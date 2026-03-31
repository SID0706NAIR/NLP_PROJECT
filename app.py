import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

# Page Config
st.set_page_config(page_title="NLP Accessibility Tool", page_icon="🎤")

st.title("🌐 NLP Accessibility Tool")
st.markdown("### Bridging Communication Gaps with Search-Based AI")

# Sidebar for Navigation (Replaces your 'while True' menu)
option = st.sidebar.selectbox(
    "Select a Module:",
    ("Project Overview", "Speech-to-Text (STT)", "Text-to-Speech (TTS)")
)

if option == "Project Overview":
    st.write("Welcome to the NLP Accessibility Tool.")
    st.info("This system uses State-Space logic to navigate between communication assistance modules.")

elif option == "Speech-to-Text (STT)":
    st.subheader("🎤 Accessibility Mode: Listening")
    st.write("Click the button below and speak into your microphone.")
    
    if st.button("Start Listening"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Recording... (5 second limit)")
            try:
                audio = recognizer.listen(source, timeout=5)
                # Using Google's Search-based decoding
                text = recognizer.recognize_google(audio)
                st.success(f"**Recognized Text:** {text}")
            except Exception as e:
                st.error(f"Error: {e}. Ensure your browser has mic permissions.")

elif option == "Text-to-Speech (TTS)":
    st.subheader("🔊 Screen Reader Mode: Speaking")
    user_text = st.text_area("Enter text to be read aloud:", placeholder="Type here...")
    
    if st.button("Convert to Speech"):
        if user_text.strip():
            # Generate the MP3 file
            tts = gTTS(text=user_text, lang='en')
            tts.save("output.mp3")
            
            # Play in the browser
            audio_file = open("output.mp3", 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
            st.success("Audio generated successfully!")
        else:
            st.warning("Please enter some text first.")

st.sidebar.divider()
st.sidebar.caption("Project for EY | Using Python & Streamlit")