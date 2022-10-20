# from main import *
import webbrowser
import speech_recognition as sr

# website = webbrowser.open("http://"+"wsj.com") #open websites

def voice_search():
    speech = sr.Recognizer()

    voice_input = ""

    with sr.Microphone() as source:

        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio) #voice input becomes spoken word

        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            pass
    return voice_input

def search_web():
    while True:
        print("Python is listening")

        inp = voice_search()
        print(f"You just said {inp}")

        if inp == "Stop listening":
            print("Goodbye")
            break

        elif "browser" in inp:
            inp = inp.replace("browser ", '')
            #webbrowser.open("http://"+inp) #concatenate strings so spoken word gets added to URl. browser google = URL + google
            webbrowser.open("http://google.com/search?q="+inp) #-> URL for google queries
            continue
