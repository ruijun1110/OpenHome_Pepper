# Import necessary modules and functions
from LLM import chatgpt  # Import the chatgpt function from the LLM (Language Learning Model) module.
from voice_input_output.text_to_voice import text_to_speech  # Convert text responses to voice.
from voice_input_output.voice_to_text import record_and_transcribe  # Convert voice inputs to text.
from add_arguments import get_initial_personality  # Parse arguments for initial personality setup.
from process_user_message import process_message  # Process user messages to determine actions.
from personalities_manager import load_personality  # Manage loading of AI personalities.
from history_files.history_manager import store_history  # Manage storage of all conversation history.
from history_files.user_memory_manager import update_recent_history  # Update recent chats for context.
from conversation_manager import manage_conversation  # Manage and track the flow of conversation.
import re  # Regular expressions for text formatting.
from colorama import Fore, Style  # Color and style for console outputs.
import yaml  # YAML file processing.
import json  # JSON file processing.

# Load configuration settings from YAML file.
with open('config.yaml', 'r', encoding='utf-8') as file:
    file_data = yaml.safe_load(file)  # Safe loading avoids executing arbitrary code.

# Initialize system based on user arguments.
personality_id = get_initial_personality()  # Get the personality ID specified by the user.
personality = load_personality(personality_id=personality_id)  # Load the corresponding personality data.

def main(personality, conversation):
    """
    Drive the main interaction loop with the user, handling voice input, processing, response generation, and voice output.

    Args:
        personality (dict): The AI personality settings including voice ID and personality traits.
        conversation (list): History of the conversation for context.

    Returns:
        tuple: Updated conversation history and a flag indicating if the chat should end.
    """
    end_chat = False  # Flag to determine if the conversation should end.
    
    if conversation:
        # Convert user's spoken words into text.
        user_message = record_and_transcribe(file_data['openai_api_key'])
        
        # Update the conversation history with the user's message.
        conversation = manage_conversation(user_message, conversation, role='user')
        
        # Process the user's message to check for commands or actions.
        is_valid_message = process_message(user_message)
        
        if not is_valid_message:
            return conversation, end_chat  # Skip response generation if message is invalid.
        
        # Generate a response using the chatgpt function.
        response = chatgpt(file_data['openai_api_key'], conversation, personality['personality'])
        print(Fore.YELLOW + f"{personality['name']}: {response}" + Style.RESET_ALL)
        
        # Store the conversation history and update recent interactions.
        store_history(user_message, response)
        update_recent_history(user_message, response)
        
        # Update conversation history with AI's response.
        conversation = manage_conversation(response, conversation, role='assistant')
        
        # Clean up the response text for voice output.
        formatted_message = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', response).strip()
    else:
        # Greet the user on the first interaction.
        formatted_message = file_data['greetings']
        conversation.append({"role": "user", "content": ''})
    
    # Convert the AI's text response to speech.
    text_to_speech(formatted_message, personality['voice_id'], file_data['elevenlabs_api_key'])
    
    return conversation, end_chat

# Initialize the conversation history.
conversation = []

# Main interaction loop.
while True:
    conversation, end_chat = main(personality, conversation)
    if end_chat:
        break  # Exit the loop if the conversation should end.
