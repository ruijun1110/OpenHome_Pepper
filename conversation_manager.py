
def manage_conversation(message, conversation, role):
    conversation.append({"role": role, "content": message})
    return conversation