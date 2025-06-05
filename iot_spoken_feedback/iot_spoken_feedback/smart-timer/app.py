import requests
import threading
import time
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer

speech_api_key = 'E9FXV9PX7CpaZtMMR1BMV0zC1N6yH5mHiJW2rnMlEaEozqSa4OYmJQQJ99BFACqBBLyXJ3w3AAAYACOGOxMS'
location = 'southeastasia'
language = 'en-GB'

recognizer_config = SpeechConfig(subscription=speech_api_key,
                                 region=location,
                                 speech_recognition_language=language)

recognizer = SpeechRecognizer(speech_config=recognizer_config)

def get_timer_time(text):
    url = 'http://192.168.51.59:7071/api/text-to-timer'

    body = {
        'text': text
    }

    response = requests.post(url, json=body)

    if response.status_code != 200:
        return 0
    
    payload = response.json()
    return payload['seconds']

def say(text):
    print(text)

def announce_timer(minutes, seconds):
    announcement = 'Times up on your '
    if minutes > 0:
        announcement += f'{minutes} minute '
    if seconds > 0:
        announcement += f'{seconds} second '
    announcement += 'timer.'
    say(announcement)

def create_timer(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    threading.Timer(total_seconds, announce_timer, args=[minutes, seconds]).start()

    announcement = ''
    if minutes > 0:
        announcement += f'{minutes} minute '
    if seconds > 0:
        announcement += f'{seconds} second '    
    announcement += 'timer started.'
    say(announcement)

def process_text(text):
    print(text)

    seconds = get_timer_time(text)
    if seconds > 0:
        create_timer(seconds)

def recognized(args):
    process_text(args.result.text)

recognizer.recognized.connect(recognized)

recognizer.start_continuous_recognition()

while True:
    time.sleep(1)