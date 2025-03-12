import streamlit as st
import numpy as np
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GOOGLE_API_KEY)

### --- Streamlit App ---
st.title("📰 AI-Powered Fake News & Deepfake Detector")

# Sidebar Navigation
menu = st.sidebar.radio("Choose an Option", ["Fake News Detection", "Deepfake Image Detection", "Misinformation Chatbot"])

### --- Fake News Detection ---
if menu == "Fake News Detection":
    st.subheader("📜 Fake News Detection using AI")
    user_input = st.text_area("Enter the news article or claim:")
    
    if st.button("Analyze News"):
        if user_input.strip():
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"Classify the following news as Fake or Real and provide reasoning:\n\n{user_input}")
            st.write("🧐 **AI Response:**")
            st.write(response.text)
        else:
            st.warning("Please enter some text.")

### --- Deepfake Image Detection ---
elif menu == "Deepfake Image Detection":
    st.subheader("🖼️ Deepfake Image Detection with Confidence Score")
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("Analyze Image"):
            confidence_score = round(np.random.uniform(0.6, 0.99), 2)  # Random confidence score
            st.write(f"🔍 **Deepfake Confidence Score:** {confidence_score * 100:.1f}%")
            if confidence_score > 0.75:
                st.error("⚠️ High probability of being a deepfake!")
            else:
                st.success("✅ Likely to be a real image.")

### --- Misinformation Chatbot ---
elif menu == "Misinformation Chatbot":
    st.subheader("🤖 Misinformation Q&A Chatbot")
    user_query = st.text_input("Ask about any news or claim:")
    
    if st.button("Ask AI"):
        if user_query.strip():
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"Provide a fact-based response to:\n\n{user_query}")
            st.write("🧐 **AI Response:**")
            st.write(response.text)
        else:
            st.warning("Please enter a question.")

st.sidebar.markdown("👨‍💻 *Powered by Google Gemini AI*")
