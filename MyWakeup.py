from constants import voice_to_text

'''
Author: Steven Vafadar (301171884), Ken Tao Zheng (301070670)
Last Modified: Steven Vafadar
Date: Dec 6th 2022
'''

'''
This is the file to put the voice assistant in "sleep" or "activated" mode. This is highly beneficial as it can wait for your 
voice inputs in the backgruond, so it could be immediately summoned without needing to open and close the application repeatedly. 
'''

#Activate + Deactivate the voice assistant

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