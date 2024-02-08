import openai
import sounddevice as sd
import soundfile as sf
# importing speech recognition library
import speech_recognition as sr

def record_and_transcribe(api_key):
    """    
    This function takes api key and records user message using speech recognition and convertssppech 
    to text using open ai and return text message.

    Args:
        api_key (string): Api key for eleven labs service.

    Returns:
        transcription (string): A string message converted from speech to text using eleven labs.
    """
    #    Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)  # You can adjust the duration as needed
        print("Recording.")
        transcription = r.listen(source)
        recording = transcription.get_wav_data()
        print("Recording Complete.")

    with open('recordings/myrecording.wav', 'wb') as file:
        file.write(recording)
    with open('recordings/myrecording.wav', 'rb') as file:
        openai.api_key = api_key
        result = openai.Audio.transcribe("whisper-1", file)
    transcription = result['text']
    print("Transcription:", transcription)  # Add this line to print the transcription
    return transcription