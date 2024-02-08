import json 

def load_personalities_json(path='personalities/personalities.json'):
    # Open the JSON file
    with open(path, 'r') as file:
        # Load JSON data from file
        personalities_json = json.load(file)
    return personalities_json

def load_personality(personality_id):
    # call load personality function to get personalties json
    personalities_json = load_personalities_json()
    # check if personality exists
    if not personality_id in personalities_json:
        print('Agent do not exists')
        print('Available list {1:Alan_watts, 2:Ava, 3:Annabele}')
        exit()
    else:
        personality = personalities_json[personality_id]
        with open(personality['personality'], 'r') as file:
            # Read the entire contents of the file into a variable
            personality_content = file.read()
        personality['personality'] = personality_content
    return personality