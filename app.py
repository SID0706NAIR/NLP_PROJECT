import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

# Page Config
st.set_page_config(page_title="NLP Accessibility Tool", page_icon="🎤")

# Sidebar for Navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Select a Module:",
    ("Project Overview", "Speech-to-Text (STT)", "Text-to-Speech (TTS)")
)

# --- MODULE 1: PROJECT OVERVIEW (MAIN SCREEN) ---
if option == "Project Overview":
    st.title("🌐 NLP Accessibility Tool")
    st.markdown("### Bridging Communication Gaps with Search-Based AI")
    
    st.info("✨ **Welcome!** This system uses State-Space logic to navigate between communication assistance modules.")

    # Main "About" Content
    st.subheader("📖 About the Project")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        #### Purpose and Use Case
        This platform is a **Digital Inclusion Tool** designed to assist users with visual or hearing impairments. 
        By leveraging Natural Language Processing (NLP), the tool acts as a bridge for bidirectional communication:
        
        * **For Hearing Impairment (STT):** Transcribes spoken words into text in real-time, allowing users to read conversation.
        * **For Visual Impairment (TTS):** Acts as a screen reader, converting written input into clear audio synthesis.
        """)
    
    with col2:
        # Adding a visual element to the main screen
        st.image("https://img.icons8.com/clouds/200/communication.png")

    st.divider()
    
    st.markdown("""
    #### 🛠️ How it Works
    The system treats communication as a **State-Space Search Problem**:
    1.  **Search-Based Decoding (STT):** When listening, the AI searches for the most likely word matches from a phonetic database.
    2.  **Synthesis Search (TTS):** The engine searches for correct phonemes to reconstruct natural human speech.
    
    *Developed for EY | Technical Research Assignment*
    """)

# --- MODULE 2: SPEECH TO TEXT ---
elif option == "Speech-to-Text (STT)":
    st.title("🎤 Accessibility Mode: Listening")
    st.write("Click the button below and speak into your microphone.")
    
    if st.button("Start Listening"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.status("Listening... (5 second limit)")
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                st.success(f"**Recognized Text:** {text}")
            except Exception as e:
                st.error(f"Error: {e}. Ensure your browser has mic permissions.")

# --- MODULE 3: TEXT TO SPEECH ---
elif option == "Text-to-Speech (TTS)":
    st.title("🔊 Screen Reader Mode: Speaking")
    user_text = st.text_area("Enter text to be read aloud:", placeholder="Type here...")
    
    if st.button("Convert to Speech"):
        if user_text.strip():
            with st.spinner("Synthesizing voice..."):
                tts = gTTS(text=user_text, lang='en')
                tts.save("output.mp3")
                
                audio_file = open("output.mp3", 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
                st.success("Audio generated!")
        else:
            st.warning("Please enter some text first.")

# Sidebar Footer