import json

class DynamicPersonalityConstructor:
    """
    DynamicPersonalityConstructor manages the dynamic generation of prompts for the AI model based on user history
    and selected personality. It supports switching personalities and tailoring responses to provide a more
    personalized interaction experience.

    Future expansion could include more advanced personality traits, mood tracking, and adaptive learning based on
    user interactions, allowing the AI to evolve its responses over time to match the user's preferences more closely.
    """

    def __init__(self, personalities_file, user_history_file):
        """
        Initializes the constructor with the given personality and user history files.
        Loads the default personality and user history upon initialization.
        """
        print("Initializing Dynamic Personality Constructor")
        self.personalities = self.load_personalities(personalities_file)
        self.user_history = self.load_user_history(user_history_file)
        self.current_personality_id = 1  # Start with default personality
        self.update_current_personality()
        print(f"Initialized with personality ID {self.current_personality_id}")

    def load_personalities(self, filepath):
        """
        Loads personality configurations from a JSON file.
        """
        print(f"Loading personalities from {filepath}")
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_user_history(self, filepath):
        """
        Loads the user's historical interaction data from a file.
        """
        print(f"Loading user history from {filepath}")
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()

    def update_current_personality(self):
        """
        Updates the current personality details based on the selected personality ID.
        """
        print(f"Updating to personality ID {self.current_personality_id}")
        personality = next((p for p in self.personalities if p["ID"] == self.current_personality_id), None)
        if personality:
            self.voice_id = personality['VoiceID']
            with open(personality['PersonalityPath'], 'r', encoding='utf-8') as file:
                self.chatbot = file.read()
            print(f"Loaded personality: {personality['Description']}")
        else:
            raise ValueError("Personality ID not found in personalities list")

    def switch_personality(self, personality_id):
        """
        Switches the current personality to the one specified by the given ID.
        """
        print(f"Switching personality to ID {personality_id}")
        self.current_personality_id = personality_id
        self.update_current_personality()

    def construct_prompt(self, user_input):
        """
        Constructs a prompt for the AI model combining the current personality, user history, and user input.
        """
        prompt = f"{self.chatbot}\n\nUser History:\n{self.user_history}\n\n{user_input}"
        print(f"Constructed prompt: {prompt[:100]}...")  # Print first 100 chars for brevity
        return prompt

# Example usage:
# personality_constructor = DynamicPersonalityConstructor("personalities/personalities.json", "history-files/user.txt")
