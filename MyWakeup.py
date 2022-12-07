from constants import voice_to_text

def wakeup():
    print("waiting to be activated")
    #inp = voice_to_text()
    inp = input("Enter something")
    wakeup = "StandBy"

    if "rise" in inp: #get list of possible wakeup commands
        wakeup = "Activated"

    elif "stop" in inp: #shut off commands
        wakeup = "ToQuit"

    return wakeup