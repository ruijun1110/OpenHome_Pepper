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
from DynamicPersonalityConstructor import DynamicPersonalityConstructor


# Colorama initialization for colored text output
init()

# Global flag to check if it's the first run of the script
# Set to True to trigger the first run experience (onboarding assistant)
# Needs to be refactored, is currently broken since I modularized personalities to DynamicPersonalityConstructor.
is_first_run = False #Keep false for now

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
personality_constructor = DynamicPersonalityConstructor('personalities/personalities.json', 'history-files/user.txt')


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
    print("Starting main loop iteration...")
    # Step 1: Record and transcribe user's voice
    print("Recording user's voice...")
    user_message = record_and_transcribe(api_key)
    print(f"Transcription: {user_message}")

    # Step 2: Process commands
    print("Processing commands...")
    command_processed, user_message, pause_main, switch_personality_requested, new_personality_id = process_command(user_message, api_key)
    print(f"Command processed: {command_processed}, Pause main: {pause_main}, Switch personality: {switch_personality_requested}")

    # Update personality if needed
    if switch_personality_requested:
        personality_constructor.switch_personality(new_personality_id)
        print(f"Switched to new personality: ID {new_personality_id}")

    # Step 3: 
    print("Appending user message to conversation history...")
    conversation1.append({"role": "user", "content": user_message})

    # Generate dynamic prompt
    print("Generating dynamic prompt...")
    dynamic_prompt = personality_constructor.construct_prompt(user_message)
    print(f"Dynamic Prompt: {dynamic_prompt[:100]}...")  # Print first 100 characters for brevity


    # Step 4: Interact with ChatGPT module
    print("Interacting with ChatGPT module...")
    start_time = datetime.datetime.now()  # Define start_time here
    response = chatgpt(api_key, dynamic_prompt, conversation1)

    voice_id1 = personality_constructor.voice_id  # Get the current voice ID


    chatgpt_response_time = datetime.datetime.now() - start_time
    print(f"Time taken for ChatGPT response: {chatgpt_response_time.total_seconds()} seconds")

    print_colored("Openhome:", f"{response}\n\n")     # Step 4b: Output response to terminal (optional)

    # Step 5: Handle text-to-speech conversion
    user_message_without_generate_image = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()
    tts_start_time = datetime.datetime.now()
    text_to_speech(user_message_without_generate_image, voice_id1, elapikey)
    tts_response_time = datetime.datetime.now() - tts_start_time
    print(f"Time taken for text-to-speech conversion (including speaking): {tts_response_time.total_seconds()} seconds")


