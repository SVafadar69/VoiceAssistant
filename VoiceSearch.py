# from main import *
import webbrowser
import speech_recognition as sr
from constants import voice_to_text, print_say

# website = webbrowser.open("http://"+"wsj.com") #open websites

def search_web():
    while True:
        print_say("What do you want me to search?")
        inp = voice_to_text()
        print(f"You just said {inp}")

        if inp == "Stop listening":
            print("Goodbye")
            break

        elif "browser" in inp:
            inp = inp.replace("browser ", '')
            #webbrowser.open("http://"+inp) #concatenate strings so spoken word gets added to URl. browser google = URL + google
            webbrowser.open("http://google.com/search?q="+inp) #-> URL for google queries
            continue

if __name__ == "__main__":
    search_web()