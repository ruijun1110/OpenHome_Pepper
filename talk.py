import sounddevice as sd
import soundfile as sf
import numpy as np
import openai
import os
import requests
import re
from colorama import Fore, Style, init
import datetime
import base64
from pydub import AudioSegment
from pydub.playback import play

init()

# Global flag to check if it's the first run of the script
is_first_run = True

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

api_key = open_file('api-keys/openaiapikey2.txt')
elapikey = open_file('api-keys/elabapikey.txt')

conversation1 = []  
chatbot1 = open_file('personalities/Activated.txt')



def chatgpt(api_key, conversation, chatbot, user_input, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
    openai.api_key = api_key
    conversation.append({"role": "user","content": user_input})
    messages_input = conversation.copy()
    prompt = [{"role": "system", "content": chatbot}]
    messages_input.insert(0, prompt[0])
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=messages_input)
    chat_response = completion['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": chat_response})

    # Write to history file
    with open('history-files/history.txt', 'a', encoding='utf-8') as history_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history_file.write(f"Timestamp: {timestamp}\n")
        history_file.write(f"User: {user_input}\n")
        history_file.write(f"Openhome: {chat_response}\n\n")

    return chat_response



def text_to_speech(text, voice_id, api_key):
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'Accept': 'audio/mpeg',
        'xi-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'model_id': 'eleven_monolingual_v1',
        'voice_settings': {
            'stability': 0.6,
            'similarity_boost': 0.85
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open('temp-sound/output.mp3', 'wb') as f:
            f.write(response.content)
        audio = AudioSegment.from_mp3('temp-sound/output.mp3')
        play(audio)
    else:
        print('Error:', response.text)

def print_colored(agent, text):
    agent_colors = {
        "Openhome:": Fore.YELLOW,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

voice_id1 = 'X9RpamxN1NCrMwRbZ0WF'

def record_and_transcribe(duration=8, fs=44100):
    print('Recording...')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print('Recording complete.')




    filename = 'temp-sound/myrecording.wav'
    sf.write(filename, myrecording, fs)
    with open(filename, "rb") as file:
        openai.api_key = api_key
        result = openai.Audio.transcribe("whisper-1", file)
    transcription = result['text']
    print("Transcription:", transcription)  # Add this line to print the transcription
    return transcription


# Function to greet the user on first run
def first_time_greeting():
    global is_first_run
    if is_first_run:
        # Read user information
        user_info = open_file('history-files/user.txt')

        # Initial greeting message
        greeting_message = "Hi Shannon. I'm excited to meet you. I'm the OpenHome onboarding assistant. Let me summarize what I know about you."

        # Pass user info to the chatbot
        chat_response = chatgpt(api_key, conversation1, chatbot1, user_info, temperature=0.5)

        # Convert chatbot's response to speech
        text_to_speech(chat_response, voice_id1, elapikey)

        is_first_run = False



# Call the first time greeting function
first_time_greeting()

while True:
    user_message = record_and_transcribe()
    response = chatgpt(api_key, conversation1, chatbot1, user_message)
    print_colored("Openhome:", f"{response}\n\n")
    user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()
    text_to_speech(user_message_without_generate_image, voice_id1, elapikey)
