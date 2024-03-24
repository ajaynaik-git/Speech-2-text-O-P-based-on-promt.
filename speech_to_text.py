# Author & Source code details

# Author - Ajay A Naik
# About code - speech to text conversion & natural voice synthesizer along with text output to user's questions. 
# If you enjoyed using the code & want to DM me just drop a message @ Linkedin (available in my git hub profile section)🙂
# Extra modules required - 3

# note - you need to get your own api key form openai.com dont worry😃 it's quite easy.

# Importing libraries
import streamlit as st
import speech_recognition as sr
import openai
import time

# Setting Webpage Configurations
st.set_page_config(page_icon="🎤",page_title="Ajay's Code", layout="wide")

st.title(":rainbow[Speech to Text with ChatGPT]🔊")

st.divider() 

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone

record = st.button(':violet[Voice Search (Click on it)] 🔍')


if record:
    with sr.Microphone() as source:
        st.caption("Say something...")
        audio = recognizer.listen(source,phrase_time_limit=3)

    # Recognize the audio
    try:
        text = recognizer.recognize_google(audio)  # You can choose a different recognition engine/API
        st.caption(f"Prompt : {text}")

    except sr.UnknownValueError:
        st.caption("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        st.caption(f"Error connecting to the recognition service: {e}")

# go to openai.com for getting a key
    openai.api_key = 'paste your openai api key here'

    prompt_text = text

    response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt = prompt_text,
    max_tokens=3500
    )

    with st.spinner('Loading....'):
        time.sleep(2)
    st.code(response['choices'][0]['text'])
    st.divider() 



