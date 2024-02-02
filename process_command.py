def process_command(transcription):
    commands = ["end session", "update brain"]
    for command in commands:
        if command in transcription.lower():
            print(f"Command '{command}' executed.")
            # Handle the command as needed
            return True, transcription
    return False, transcription
