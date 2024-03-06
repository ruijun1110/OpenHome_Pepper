# Import necessary modules and functions
from LLM import chatgpt  # Import the chatgpt function from the LLM (Language Learning Model) module.
from voice_input_output.text_to_voice import text_to_speech  # Convert text responses to voice.
from voice_input_output.text_to_voice import text_to_speech_mimic
from voice_input_output.voice_to_text import record_and_transcribe  # Convert voice inputs to text.
from add_arguments import get_args  # Parse arguments for initial personality setup.
from process_user_message import process_message  # Process user messages to determine actions.
from personalities_manager import load_personality  # Manage loading of AI personalities.
from history_files.history_manager import store_history  # Manage storage of all conversation history.
from history_files.user_memory_manager import update_recent_history  # Update recent chats for context.
from conversation_manager import manage_conversation  # Manage and track the flow of conversation.
import re  # Regular expressions for text formatting.
from colorama import Fore, Style  # Color and style for console outputs.
import yaml  # YAML file processing.
import json  # JSON file processing.
import capabilities.get_news as get_news  # Import the get_news function from the capabilities module.
import capabilities.google_calendar as google_calendar  # Import the google_calendar function from the capabilities module.
import datetime
import pytz

# Load configuration settings from YAML file.
with open('config.yaml', 'r', encoding='utf-8') as file:
    file_data = yaml.safe_load(file)  # Safe loading avoids executing arbitrary code.
voice_id = 'OYWAX2pWZtnMdoUwxIkN'
elevenlabs_api = '15dec7728128dcdc7254dcfa7c1ab947'
# Initialize system based on user arguments.
args = get_args()
initial_personality = load_personality(personality_id=args.personality)  # Load the corresponding personality data.
personality = "Your primary responsibility as my long-term assistant is to efficiently manage my schedule using the calendar data provided following [Calendar]. When addressing schedule-related inquiries, please prioritize concise and professional communication while ensuring time efficiency. You can assume I am aware of the events, so you don't have to mention complete event details, just provide a brief reminder. It is crucial to strike a balance between professionalism and efficiency in your interactions. Provide responses in a conversational tone without simply listing information."
def main(personality, conversation, no_audio=False):
    """
    Drive the main interaction loop with the user, handling voice input, processing, response generation, and voice output.

    Args:
        personality (dict): The AI personality settings including voice ID and personality traits.
        conversation (list): History of the conversation for context.

    Returns:
        tuple: Updated conversation history and a flag indicating if the chat should end.
    """
    end_chat = False  # Flag to determine if the conversation should end.
    # Create a timezone-aware datetime object for the current time in UTC
    utc_now = datetime.datetime.now(pytz.utc)

    # Convert the timezone-aware datetime object to PST
    pst_now = utc_now.astimezone(pytz.timezone('US/Pacific'))

    if conversation:
        
        # Convert user's spoken words into text.
        if no_audio:
            user_message = input("User: ")
        else:
            user_message = record_and_transcribe(file_data['openai_api_key'])      
        # Process the user's message to check for commands or actions.
        # is_valid_message = process_message(new_user_message)
        
        # if not is_valid_message:
        #     return conversation, end_chat  # Skip response generation if message is invalid.
        
        # Generate a response using the chatgpt function.
            
        conversation = manage_conversation(user_message, conversation, role='user')

        response = chatgpt(file_data['openai_api_key'], conversation, initial_personality['personality'], temperature=1.2)
        print(Fore.CYAN + f"{initial_personality['name']}: {response}" + Style.RESET_ALL)
        final_user_message = user_message
        # "<task>,<[summarized command]>,<[acknowledgement]>" 
        if "<task>" in response:
            command = response.split("<")[2]
            response = response.split("<")[3]
            conversation = manage_conversation(response, conversation, role='assistant')
            text_to_speech(response, voice_id, elevenlabs_api)
            system_response = google_calendar.command_processing(file_data, command)
            print(Fore.CYAN + f"System: {system_response}" + Style.RESET_ALL)
            conversation = manage_conversation(system_response, conversation, role='system')
            print("Conversation passed to OpenAI:" + conversation)
            final_response = chatgpt(file_data['openai_api_key'], conversation, initial_personality['personality'], temperature=1.2)
            print(Fore.CYAN + f"{initial_personality['name']}: {final_response}" + Style.RESET_ALL)
        else:
            final_response = response

        # Store the conversation history and update recent interactions.
        store_history(final_user_message,final_response)
        update_recent_history(final_user_message, final_response)
        
        # Update conversation history with AI's response.
        conversation = manage_conversation(final_response, conversation, role='assistant')
        
        # Clean up the response text for voice output.
        formatted_message = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '', final_response).strip()
    else:
        # Greet the user on the first interaction.
        formatted_message = file_data['greetings']
        conversation.append({"role": "user", "content": ''})
   
    # Convert the AI's text response to speech.
    if not no_audio:
    #   text_to_speech(formatted_message, personality['voice_id'], file_data['elevenlabs_api_key'])
        text_to_speech(formatted_message, voice_id, elevenlabs_api )
    return conversation, end_chat

# Initialize the conversation history.
conversation = []

def get_current_datetime():
    now = datetime.datetime.utcnow()
    pst = pytz.timezone('America/Los_Angeles')
    now_pst = now.astimezone(pst).isoformat()
    weekday = now.astimezone(pst).strftime("%A")
    return now_pst, weekday

# Main interaction loop.
while True:
    conversation, end_chat = main(personality, conversation, args.no_audio)
    if end_chat:
        break  # Exit the loop if the conversation should end.
