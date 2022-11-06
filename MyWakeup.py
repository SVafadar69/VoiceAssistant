from constants import voice_to_text

def wakeup():
    print("waiting to be ")
    #inp = voice_to_text()
    inp = "rise"
    wakeup = "StandBy"

    if "rise" in inp: #get list of possible wakeup commands
        wakeup = "Activated"

    elif "stop" in inp:
        wakeup = "ToQuit"

    return wakeup