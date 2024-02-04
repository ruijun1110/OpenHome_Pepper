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
import json
from pydub import AudioSegment
from pydub.playback import play
from file_management import open_file, write_to_file

# Importing custom modules
from chatgpt_module import chatgpt
from greeting_module import first_time_greeting
from text_speech_module import text_to_speech
from audio_module import record_and_transcribe
from process_command import process_command

# Colorama initialization for colored text output
init()

# Global flag to check if it's the first run of the script
# Set to True to trigger the first run experience (onboarding assistant)
is_first_run = True

# ---------------------
# Function Definitions
# ---------------------

def load_personalities(filepath):
    """Load the personalities configuration from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

# ---------------------
# Configuration and Setup
# ---------------------

# Load API keys from files
api_key = open_file('api-keys/openaiapikey2.txt')
elapikey = open_file('api-keys/elabapikey.txt')

# Load and select the default personality
personalities = load_personalities('personalities/personalities.json')
default_personality_id = 1  # Default personality ID
current_personality = personalities[default_personality_id - 1]
voice_id1 = current_personality['VoiceID']
chatbot1 = open_file(current_personality['PersonalityPath'])

# Load content for the onboarding guide (In the future this should only load if it's the first run)
onboarding_guide_path = 'personalities/onboarding.txt'  # Update with the correct path
onboarding_guide = open_file(onboarding_guide_path)
onboarding_voice_id = 'SQexbWhyaGEi9hIBqXqM'  # Replace with your actual onboarding voice ID # Define the voice ID for the onboarding process

# Load API keys
api_key = open_file('api-keys/openaiapikey2.txt')
elapikey = open_file('api-keys/elabapikey.txt')

# Initialize conversation histories for different personalities
conversation1 = []  # Main conversation history
conversation_onboarding = []  # Onboarding conversation history

# ---------------------
# Utility Functions
# ---------------------

def print_colored(agent, text):
    """Print text in a color based on the agent speaking."""
    agent_colors = {"Openhome:": Fore.YELLOW}
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

# ---------------------
# First Run Check
# ---------------------

if is_first_run:
    first_time_greeting(api_key, elapikey, onboarding_guide, conversation_onboarding, onboarding_voice_id)
    is_first_run = False

# ---------------------
# Main Application Loop
# ---------------------

while True:
    # Step 1: Record and transcribe user's voice
    user_message = record_and_transcribe(api_key)

    # Step 2: Process commands (like end session, update brain, etc.)
    command_processed, user_message, pause_main, switch_personality_requested, new_personality_id = process_command(user_message, api_key)

    if pause_main:
        continue  # Skip to the next iteration if main processing needs to be paused

    # Step 3: Handle personality switching
    if switch_personality_requested:
        current_personality = personalities[new_personality_id - 1]
        voice_id1 = current_personality['VoiceID']
        chatbot1 = open_file(current_personality['PersonalityPath'])
        print(f"Switched to new personality: ID {new_personality_id}")

    # Step 4: Interact with ChatGPT module
    start_time = datetime.datetime.now()
    response_note = "Command processed. " if command_processed else ""
    response = chatgpt(api_key, conversation1, chatbot1, response_note + user_message)
    chatgpt_response_time = datetime.datetime.now() - start_time
    print(f"Time taken for ChatGPT response: {chatgpt_response_time.total_seconds()} seconds")

    print_colored("Openhome:", f"{response}\n\n")     # Step 4b: Output response to terminal (optional)

    # Step 5: Handle text-to-speech conversion
    user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()
    tts_start_time = datetime.datetime.now()
    text_to_speech(user_message_without_generate_image, voice_id1, elapikey)
    tts_response_time = datetime.datetime.now() - tts_start_time
    print(f"Time taken for text-to-speech conversion (including speaking): {tts_response_time.total_seconds()} seconds")


