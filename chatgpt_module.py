from openai import OpenAI
import datetime

def chatgpt(api_key, dynamic_prompt, conversation, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
    """
    Generates a response from the GPT model based on the dynamic prompt and the ongoing conversation.

    Args:
    - api_key: API key for OpenAI.
    - dynamic_prompt: The prompt that includes personality and user history.
    - conversation: A list of message dictionaries representing the conversation history.
    - temperature, frequency_penalty, presence_penalty: Parameters to control the GPT model's behavior.

    Returns:
    - The GPT model's response as a string.
    """

    # Print debug information
    print("Inside chatgpt function...")
    print(f"Dynamic Prompt: {dynamic_prompt[:100]}...")  # Print first 100 characters for brevity
    print(f"Conversation: {conversation}")

    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key, base_url="https://chat-router.recursal-dev.com/dFe6VG2eAjfEjGt7yb39q")

    # Prepare the messages input for the GPT model by combining the dynamic prompt and conversation history
    messages_input = [{"role": "system", "content": dynamic_prompt}] + conversation

    # Make a request to the GPT model
    completion = client.chat.completions.create(
        model="gpt-4",
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=messages_input)

    # Extract the response from the completion
    chat_response = completion.choices[0].message.content

    # Append the GPT model's response to the conversation
    conversation.append({"role": "assistant", "content": chat_response})

    # Write the latest exchange (user and assistant) to the history file
    with open('history-files/history.txt', 'a', encoding='utf-8') as history_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for message in conversation[-2:]:  # Last exchange (user and assistant)
            history_file.write(f"Timestamp: {timestamp}\n")
            history_file.write(f"{message['role'].capitalize()}: {message['content']}\n")
        history_file.write("\n")

    # Return the response
    return chat_response
