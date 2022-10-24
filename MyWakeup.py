from constants import inp

def wakeup():
    print("waiting to be ")
    wakeup = "StandBy"

    if "rise and shine" in inp: #get list of possible wakeup commands
        wakeup = "Activated"

    elif "stop" in inp:
        wakeup = "ToQuit"

    return wakeup