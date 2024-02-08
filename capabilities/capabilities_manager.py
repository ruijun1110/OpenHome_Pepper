import json 
from capabilities.end_session import end_session
def load_capabilities_json(path='capabilities/capabilities.json'):
    # Open the JSON file
    with open(path, 'r') as file:
        # Load JSON data from file
        capabilities_json = json.load(file)
    return capabilities_json

def check_and_perform_action(message):
    capabilities_json = load_capabilities_json()
    action = {}
    # conver message to lower case to handle matching exception.
    message = message.lower()

    for capability in capabilities_json:
        # GET Capability of ending our conversation.
        if capability['Command'] == 'End session':
            end_chat_words = capability['Triggers']
            # if any ending word in list is peresent in user message end the chat.
            exit_flag = any(word in message for word in end_chat_words)
            if exit_flag:
                end_session()
