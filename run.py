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

# Importing custom modules
from chatgpt_module import chatgpt
from greeting_module import first_time_greeting
from text_speech_module import text_to_speech
from audio_module import record_and_transcribe
from process_command import process_command

# Initialize colorama for colored text output
init()

# Global flag to check if it's the first run of the script
is_first_run = False

# Function to open and read a file
def open_file(filepath):
    """Open and return the content of a file given its filepath."""
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Load API keys and voice ID from files
api_key = open_file('api-keys/openaiapikey2.txt')
elapikey = open_file('api-keys/elabapikey.txt')

voice_id1 = 'Ii3OgQbD90mchULEEqmA' #Main
onboarding_voice_id = 'SQexbWhyaGEi9hIBqXqM' #Personality Builder

# Initialize conversation history and load chatbot personality
conversation1 = []  
conversation_onboarding = []  
chatbot1 = open_file('personalities/34e00e46-0dcc-4d42-9d3a-217426b62e73.txt')
onboarding_guide = open_file('personalities/Onboarding.txt')


# Function to print text in colored format
def print_colored(agent, text):
    """Print the text in a color based on the agent speaking."""
    agent_colors = {"Openhome:": Fore.YELLOW}
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

# Check if this is the first run of the script
if is_first_run:
    # Perform first time greeting using the greeting module
    first_time_greeting(api_key, elapikey, onboarding_guide, conversation_onboarding, onboarding_voice_id)
    is_first_run = False



# Main loop
while True:
    # Record user's voice and transcribe it
    user_message = record_and_transcribe(api_key)

    # Check and process specific commands before sending to ChatGPT (end session, update brain, etc)
    # Process the command if present
    command_processed, user_message, pause_main = process_command(user_message, api_key)

    if pause_main:
        # Skip the rest of the loop if the main thread should pause
        continue

    # Start timing just before sending the request to ChatGPT
    start_time = datetime.datetime.now()

    # Generate a response using the ChatGPT module
    # Include a note in the user_message if a command was processed
    response_note = "You are a smart speaker. Tell me that you just processed a command. My message to you follows:" if command_processed else ""
    response = chatgpt(api_key, conversation1, chatbot1, response_note + user_message)

    # Calculate the time taken for ChatGPT to respond
    chatgpt_response_time = datetime.datetime.now() - start_time
    print(f"Time taken for ChatGPT response: {chatgpt_response_time.total_seconds()} seconds")

    # Print the response in a colored format
    print_colored("Openhome:", f"{response}\n\n")

    # Remove any image generation commands from the response
    user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()

    # Start timing the text-to-speech conversion
    tts_start_time = datetime.datetime.now()

    # Convert the response to speech and play it
    text_to_speech(user_message_without_generate_image, voice_id1, elapikey)

    # Calculate the time taken for text-to-speech conversion
    tts_response_time = datetime.datetime.now() - tts_start_time
    print(f"Time taken for text-to-speech conversion (including speaking): {tts_response_time.total_seconds()} seconds")
