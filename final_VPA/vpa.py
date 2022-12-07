from chapterSeven import *
from constants import print_say
from constants import voice_to_text
from constants import json
from constants import switch_voices
from MyWakeup import wakeup
# from jokes import joke
from AdvancedVPA import ask_wolf #will also call repeat_exception
#from emails import send_email
from news_hs import speak_news
from openAI import conversation
from onlineradio import live_radio
#from openingFiles import open_file
from constants import switch_voices
#from traverse import function
#from Turtle import screen_setup
from VoiceSearch import search_web
from wikisearch import wiki_search
#from market_watch import bitcoinwatch, stock_watch #import func directly from folder. NO need to call file
#from finance import get_stock_info, alpha_beta
#from mrworldwide import mr_worldwide_mmm

'''
Author: Steven Vafadar (301171884), Ken Tao Zheng (301070670)
Last Modified: Ken Tao Zheng
Date: Dec 6th 2022
'''

'''
This is the general assistant file, where the key functions of the application are all consolidated here. Whether it is using OpenAI's 
AIs, Wolfram Alpha's Search Engine, playing the news, or performing general google searches, all the functions of the applications
are stored in this file. 
'''

# Open chats.json and put it in a dictionary
with open('chats.json','r') as content:
    chats = json.load(content)

while True:
    # Capture your voice command quietly in standby
    wake_up = wakeup()
    # You can wake up the VPA by saying "Hello Python"
    while wake_up == "Activated":
        print_say("How may I help you?")
        #inp = voice_to_text().lower()
        inp = str(input("Enter something"))
        print_say(f'You just said {inp}.')
        if "back" in inp and "stand" in inp:
            print_say('OK, back to standby; let me know if you need help!')
            break #will break activated loop. originally infinite loop still running

        # # Activate the timer
        # elif "timer for" in inp and ("hour" in inp or "minute" in inp):
        #     timer(inp)
        #     continue
        # # Activate the alarm clock
        # elif "alarm for" in inp and ("a.m." in inp or "p.m." in inp):
        #     alarm(inp)
        #     continue
        # # Activate the joke-telling functionality
        # elif "joke" in inp:
        #     joke()
        #     continue
        elif "conversation" in inp:
            print_say("Activating conversation mode")
            conversation()
        elif len(inp) > 10: #to ensure if nothing is said (empty string) voice assistant doesn't call other methods
            print_say("Using Wolfram Alpha")
            ask_wolf()
        # elif "email" in inp:
        #     send_email()
        elif "news" in inp:
            print_say("Switching to news")
            speak_news()
        elif "live radio" in inp:
            live_radio()
        # elif "open file" in inp:
        #     open_file()
        # elif "tic tac toe" in inp:
        #     screen_setup()
        elif "search" in inp:
            search_web()
        elif "wikipedia" in inp: #don't call funcs within files to not have them run on import
            wiki_search()
        elif "switch voices" in inp:
            switch_voices()
        # elif "bitcoin watch" in inp:
        #     bitcoinwatch()
        # elif "stock watch" in inp:
        #     stock_watch()
        # # Activate the email-sending functionality
        # elif "send" in inp and "email" in inp:
        #     email()
        #     continue
        # else:
        #     continue
    # End the script by including "stop" in your voice
    if wake_up == "ToQuit":
        print_say("OK, exit the program; goodbye!")
        break