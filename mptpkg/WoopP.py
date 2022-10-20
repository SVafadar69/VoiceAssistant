import pyttsx3

try:
    engine = pyttsx3.init()
except(ImportError, RuntimeError):
    pass

def print_say(txt):
    print(txt) #printing the spoken word
    engine.say(txt)
    engine.runAndWait()
