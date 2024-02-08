from LLM import chatgpt
from voice_input_output.text_to_voice import text_to_speech

from voice_input_output.voice_to_text import record_and_transcribe

# add_arguments file adds argumnets to our script.
from add_arguments import get_initial_personality

# import process_user_message modeule to make decisions
from process_user_message import process_message

# import personalties manager
from personalities_manager import load_personality

# all time history manager
from history_files.history_manager import store_history

# recent two chats storage maanger
from history_files.user_memory_manager import update_recent_history

# import conversation manager to manage and converge messages
from conversation_manager import manage_conversation
import re
from colorama import Fore, Style
import yaml
import json

# Open the yaml file
with open('config.yaml', 'r', encoding='utf-8') as file:
    # Load all the data from the YAML file
    file_data = yaml.safe_load(file)

# call the function for adding arguments to this script and get arguments value passed from user.
personality_id =  get_initial_personality()

# get the personality dictioanry.
personality = load_personality(personality_id=personality_id)


# define the main function to call all functions pressetn in modules
def main(personality, conversation):
    """    
    Main function takes personality and consersation to run the whole proceses for the passed conversation using specified 
    personality.

    Args:
        personality (string): Personality entered y user while running the main script.
        conversation (list): List of messages from user and asistant as a history.

    Returns:
        conversation (list): Updated list of messages from user and asistant as a history.
        end_chat (Boolean): A falg to know whether to end the chat or not.
    """
    end_chat = False
    # if conversation has something record user data else say greetings.
    if conversation:
        # call record_and_transcribe to record user and convert it to text
        user_message = record_and_transcribe(file_data['openai_api_key'])

        # call the conversation manager to mantin conversation
        conversation = manage_conversation(user_message, conversation, role='user')

        # pass user message to process_message function to perform capabities if one triggered
        is_valid_message = process_message(user_message)
        # if message is empty return from here into main.
        if not is_valid_message:
            return conversation, end_chat

        # call chatgpt function
        response = chatgpt(file_data['openai_api_key'], conversation, personality['personality'])
        print(Fore.YELLOW + f"{personality['name']}: {response}" + Style.RESET_ALL, end="'\n")
        # log all history
        store_history(user_message, response)
        # update recent history
        update_recent_history(user_message, response)
        # call the conversation manager to mantin conversation
        conversation = manage_conversation(response,conversation, role='assistant')

        # format the mesage to remove unsed characters from the chat gpt response.
        formatted_message = re.sub(r'(Response:|Narration:|Image: generate_image:.*|)', '',response).strip()
    else:
        # on first iteration this code runs to say the greesting stored in yaml file
        formatted_message = file_data['greetings']
        # adding a empty propmt in conversation just to signify the first iteration.
        conversation.append({"role": "user", "content": ''})
    # call text to speech function to convert chat gpt text to speech
    text_to_speech(formatted_message, personality['voice_id'], file_data['elevenlabs_api_key'])
    return conversation, end_chat

conversation = []
while True:
    conversation, end_chat = main(personality, conversation)
    if end_chat:
        exit()

    