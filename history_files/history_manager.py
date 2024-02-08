import json

def store_history(user_message, assitant_message):
    new_user_message = {
        "role": "user",  # user message
        "content": user_message
    }

    new_assitant_message = {
        "role": "assistant",  # assistant message
        "content": assitant_message
    }

    # Load existing history
    with open('history_files/history.json', 'r') as file:
        history = json.load(file)

    # Append the new message to the existing history
    history['messages'].append(new_user_message)
    history['messages'].append(new_assitant_message)

    # Write the updated history back to the file
    with open('history_files/history.json', 'w') as file:
        json.dump(history, file, indent=4)