import speech_recognition as sr

speech = sr.Recognizer()
def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio) #can change language to whatever - language='en'
        except (sr.UnknownValueError, sr.RequestError ,sr.WaitTimeoutError):
            pass
    return voice_input