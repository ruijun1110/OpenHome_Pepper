import uuid  # Add this line to import the uuid module
import os

from chatgpt_module import chatgpt
from file_management import open_file, write_to_file  # Assuming you have a write_to_file function
from text_speech_module import text_to_speech
from audio_module import record_and_transcribe  # Assuming this module returns user's spoken input as text

def first_time_greeting(api_key, elapikey, onboarding_guide, conversation_onboarding, onboarding_voice_id):
    print("Running greeting module...")  # Debug message

    # Read user information
    user_info = open_file('history-files/user.txt')

    # Debug: Print contents of Onboarding Guide
    print("Contents of onboarding guide:")
    print(onboarding_guide)

    # Initial greeting message
    greeting_message = "I'm your guide. I'm the OpenHome onboarding assistant. I'll help craft you the perfect personality to interact with!"
    
    # Starting the onboarding conversation
    conversation_onboarding.append({"role": "system", "content": greeting_message})
    text_to_speech(greeting_message, onboarding_voice_id, elapikey)

    # Define questions to ask the user
    questions = [
        "Do you want a male voice or female voice?",
        "What type of personality do you want your AI to have?",
        "Do you have any celebrities or public figures you want to model your AI off of?",
        "Anything else you want to inject into its starting personality?"
    ]

    # Loop to ask questions and record answers
    for question in questions:
        # Ask each question
        text_to_speech(question, onboarding_voice_id, elapikey)
        conversation_onboarding.append({"role": "system", "content": question})

        # Record user's response
        user_response = record_and_transcribe(api_key)
        conversation_onboarding.append({"role": "user", "content": user_response})

        # Use ChatGPT for a brief response based on the user's answer
        response_prompt = f"Based on the user's response, provide a brief and engaging acknowledgment:"
        chat_response = chatgpt(api_key, conversation_onboarding, onboarding_guide, response_prompt, temperature=0.5)
        text_to_speech(chat_response, onboarding_voice_id, elapikey)
        conversation_onboarding.append({"role": "system", "content": chat_response})

    # Save conversation to a file
    conversation_file = 'history-files/new_personality_convo.txt'
    write_to_file(conversation_file, conversation_onboarding)

    # Generate AI personality from the conversation
    generate_ai_personality(api_key, conversation_file, 'personalities', onboarding_guide, conversation_onboarding)

def generate_ai_personality(api_key, conversation_file, save_path, onboarding_guide, conversation_onboarding):
    # Read the conversation
    conversation_content = open_file(conversation_file)

    # Create a prompt for ChatGPT to generate the AI personality
    prompt = f"Based on the following conversation, create a personality for a voice assistant:\n\n{conversation_content}"

    # Generate the personality using ChatGPT
    ai_personality = chatgpt(api_key, conversation_onboarding, onboarding_guide, prompt, temperature=0.5)

    # Generate a unique filename
    filename = f"{uuid.uuid4()}.txt"  # This will create a unique file name

    # Format the AI personality as expected by write_to_file
    formatted_personality = [{"role": "system", "content": ai_personality}]

    # Save the generated personality
    write_to_file(os.path.join(save_path, filename), formatted_personality)

    print(f"AI personality saved as {filename}")


# Add any necessary imports at the top of your file
