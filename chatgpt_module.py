from openai import OpenAI
import datetime

# You might need to adjust the imports based on what the chatgpt function uses

def chatgpt(api_key, conversation, chatbot, user_input, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
    client = OpenAI(api_key=api_key, base_url="https://chat-router.recursal-dev.com/dFe6VG2eAjfEjGt7yb39q")
    conversation.append({"role": "user", "content": user_input})
    messages_input = conversation.copy()
    prompt = [{"role": "system", "content": chatbot}]
    messages_input.insert(0, prompt[0])
    completion = client.chat.completions.create(
        model="gpt-4",
        temperature=temperature,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        messages=messages_input)
    chat_response = completion.choices[0].message.content
    conversation.append({"role": "assistant", "content": chat_response})

    # Write to history file
    with open('history-files/history.txt', 'a', encoding='utf-8') as history_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        history_file.write(f"Timestamp: {timestamp}\n")
        history_file.write(f"User: {user_input}\n")
        history_file.write(f"Openhome: {chat_response}\n\n")

    return chat_response
