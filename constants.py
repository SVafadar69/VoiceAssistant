import random
import json
import time
import wolframalpha
import openai
import wikipedia
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
speech = sr.Recognizer()
import ssl
import smtplib
from email.message import EmailMessage
import sys
import os
import json

##Setting up news scraping

##Setting up Wolfram Alpha Data
API_KEY = "595KVV-JY64RGJKEG"
wolf = wolframalpha.Client("595KVV-JY64RGJKEG")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
headers = {
    "User-Agent": "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8" }

def switch_voices():

    x = [1, 2]
    engine = pyttsx3
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #0= male, 1 = female. indexing list
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.8)


#Using voice as inputs
def voice_to_text():
    #print_say("Say something") #func can be called from another func that is later defined
    print("Listening to your input")
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio) #can change language to whatever - language='en'
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            pass
    return voice_input

#Computer speaking
def print_say(txt):
    try:
        engine = pyttsx3.init()
    except(ImportError, RuntimeError):
        pass

    print(txt) #printing the spoken word
    engine.say(txt)
    engine.runAndWait()

inp = voice_to_text()  # if placing a later defined func inside of voice_text, inp must be called later\

#Keep variables and functions
if __name__ == "__main__":
    print_say()
    inp
    voice_to_text()
    switch_voices()
    API_KEY
    wolf
    url
    headers