import json
import importlib.util
import sys
import os

def process_command(transcription):
    # Load commands from the JSON file
    with open('capabilities/capabilities.json', 'r') as file:
        commands = json.load(file)

    # Iterate over the commands to find a match
    for command in commands:
        for trigger in command['Triggers']:
            if trigger.lower() in transcription.lower():
                print(f"Command '{command['Command']}' executed.")

                # Build the module path
                module_name = command['Library'].replace('.py', '')
                module_path = os.path.join(os.getcwd(), module_name + '.py')  # Adjust path as necessary

                # Check if the module exists
                if not os.path.exists(module_path):
                    print(f"Module {module_name} not found.")
                    return True, transcription

                # Dynamically import the module
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                module.execute()  # Execute the module function
                return True, transcription

    return False, transcription
