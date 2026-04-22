import streamlit as st
import google.generativeai as genai

# إعداد الـ API من ملف الأسرار
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error("API Key missing! Check .streamlit/secrets.toml")

st.title("🤖 Talk With AI")
st.caption("Your Startup Hub Personal Assistant")

# وظيفة لإحضار أول موديل متاح وشغال فعلياً
def get_working_model():
    try:
        # بنجيب كل الموديلات اللي بتدعم توليد النصوص
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # بنفضل استخدام flash لأنه الأسرع والأكثر استقراراً في النسخة المجانية
        for name in available:
            if 'flash' in name:
                return name
        return available[0] if available else "models/gemini-1.5-flash"
    except:
        return "models/gemini-1.5-flash"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # بنختار الموديل ونولد الرد
            model_name = get_working_model()
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.error("جوجل لم توفر رداً حالياً، جرب رسالة أخرى.")
        except Exception as e:
            if "429" in str(e):
                st.error("السيرفر مضغوط (Quota Exceeded). استنى 60 ثانية بالضبط وجرب تاني.")
            elif "404" in str(e):
                st.error("الموديل غير متاح حالياً، جاري محاولة التبديل...")
                st.rerun()
            else:
                st.error(f"حدث خطأ: {e}")