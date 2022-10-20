from mysr import voice_to_text
from mysay import print_say
import speech_recognition as sr
speech = sr.Recognizer()
import time

import pyttsx3

engine = pyttsx3.init()

def settings():
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id) #0= male, 1 = female. indexing list
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)

settings()

# while True:

print("Say something")
inp = voice_to_text()

if "hello" in inp:
    print_say(f"You just said {inp}, goodbye!")
    engine.runAndWait()
    # break

print_say(f"You just said {inp}") #function to print spoken word, repeat the spoken word, and receive all input

