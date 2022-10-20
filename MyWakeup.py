import speech_recognition as sr

speech = sr.Recognizer()

def wakeup():

    wakeup = "StandBy"

    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source, timeout=3)
            voice_input = speech.recognize_google(audio)
        except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
            pass
        if "hello" in voice_input and "python" in voice_input:
            wakeup = "Activated"
        elif "stop" in voice_input:
            wakeup = "ToQuit"
        return wakeup