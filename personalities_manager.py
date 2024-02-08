import json

# Function to load personalities from a JSON file
def load_personalities_json(path='personalities/personalities.json'):
    # Open the JSON file containing personality definitions
    with open(path, 'r') as file:
        # Load the contents of the file into a Python dictionary
        personalities_json = json.load(file)
    # Return the loaded personalities dictionary
    return personalities_json

# Function to load a specific personality based on a given ID
def load_personality(personality_id):
    # Convert the personality_id to a string to ensure compatibility with JSON keys
    personality_id_str = str(personality_id)
    
    # Load all personalities from the JSON file
    personalities_json = load_personalities_json()
    
    # Check if the requested personality_id exists in the loaded personalities
    if personality_id_str not in personalities_json:
        # If not found, list all available personalities for debugging or user information
        available = ', '.join([f'{id}:{details["name"]}' for id, details in personalities_json.items()])
        print(f'Agent does not exist. Available list: {available}')
        # Raise an error indicating the specified personality was not found
        raise ValueError(f'Personality with ID {personality_id} not found.')
    else:
        # If found, retrieve the specific personality information
        personality = personalities_json[personality_id_str]
        # Load the personality content from the specified file within the personality dictionary
        with open(personality['personality'], 'r') as file:
            personality_content = file.read()
        # Replace the file path with its content in the 'personality' key
        personality['personality'] = personality_content
    
    # Return the fully loaded personality information, including its content
    return personality
