import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

# Page Config
st.set_page_config(page_title="NLP Accessibility Tool", page_icon="🎤")

st.title("🌐 NLP Accessibility Tool")
st.markdown("### Bridging Communication Gaps with Search-Based AI")

# Sidebar for Navigation
option = st.sidebar.selectbox(
    "Select a Module:",
    ("Project Overview", "Speech-to-Text (STT)", "Text-to-Speech (TTS)", "About this Tool")
)

if option == "Project Overview":
    st.write("Welcome to the NLP Accessibility Tool.")
    st.info("This system uses State-Space logic to navigate between communication assistance modules.")
    st.image("https://img.icons8.com/clouds/200/artificial-intelligence.png", width=200)

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

# --- NEW SECTION: ABOUT THIS TOOL ---
elif option == "About this Tool":
    st.subheader("📖 About the Project")
    st.markdown("""
    ### Purpose and Use Case
    This website is designed as a **Digital Inclusion Tool** to assist users with visual or hearing impairments. 
    By leveraging Natural Language Processing (NLP), the tool acts as a bridge for bidirectional communication:
    
    1. **For Hearing Impairment:** The Speech-to-Text (STT) module transcribes spoken words into text in real-time, allowing users to read what is being said.
    2. **For Visual Impairment:** The Text-to-Speech (TTS) module acts as a screen reader, converting written input into clear audio.
    
    ### How it Works
    The system treats communication as a **State-Space Search Problem**:
    * **Search-Based Decoding:** When listening, the AI searches for the most likely word matches from a vast phonetic database.
    * **Synthesis Search:** When speaking, the engine searches for the correct phonemes to reconstruct natural human speech.
    
    Developed as part of an EY technical assignment to showcase accessibility-first software design.
    """)

# Sidebar Footer
st.sidebar.divider()
with st.sidebar.expander("Quick Help"):
    st.write("Use STT if you need to read audio. Use TTS if you need to hear text.")
st.sidebar.caption("Developed for EY | Powered by Python & Streamlit")