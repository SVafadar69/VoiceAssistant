from constants import voice_to_text
from constants import print_say
import speech_recognition as sr
speech = sr.Recognizer()
import time

import pyttsx3

engine = pyttsx3.init()



# while True:

print("Say something")
inp = voice_to_text()

if "hello" in inp:
    print_say(f"You just said {inp}, goodbye!")
    engine.runAndWait()
    # break

print_say(f"You just said {inp}") #function to print spoken word, repeat the spoken word, and receive all input

