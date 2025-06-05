import time
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer

speech_api_key = 'E9FXV9PX7CpaZtMMR1BMV0zC1N6yH5mHiJW2rnMlEaEozqSa4OYmJQQJ99BFACqBBLyXJ3w3AAAYACOGOxMS'
location = 'southeastasia'
language = 'en-GB'


recognizer_config = SpeechConfig(subscription=speech_api_key,
                                 region=location,
                                 speech_recognition_language=language)

from azure.cognitiveservices.speech import AudioConfig

audio_config = AudioConfig(use_default_microphone=True)
recognizer = SpeechRecognizer(speech_config=recognizer_config, audio_config=audio_config)

def process_text(text):
    print(text)

def recognized(args):
    process_text(args.result.text)

recognizer.recognized.connect(recognized)

recognizer.start_continuous_recognition()

while True:
    time.sleep(1)