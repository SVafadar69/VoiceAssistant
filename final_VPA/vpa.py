from chapterSeven import *
import random
import json
from mysr import voice_to_text
from mysay import print_say
from MyWakeup import wakeup
from jokes import joke
from AdvancedVPA import ask_wolf
from emails import send_email
from news_hs import speak_news
from onlineradio import live_radio
from openingFiles import open_file
from talkback import settings
#from traverse import function
from Turtle import screen_setup
from VoiceSearch import search_web
from wikisearch import wiki_search
from market_watch import bitcoinwatch, stock_watch #import func directly from folder. NO need to call file
#from finance import get_stock_info, alpha_beta
#from mrworldwide import mr_worldwide_mmm
settings()

# Open chats.json and put it in a dictionary
with open('chats.json','r') as content:
    chats = json.load(content)

while True:
    # Capture your voice command quietly in standby
    wake_up = wakeup()
    # You can wake up the VPA by saying "Hello Python"
    while wake_up == "Activated":
        print_say("How may I help you?")
        inp = voice_to_text().lower()
        print_say(f'You just said {inp}.')
        if "back" in inp and "stand" in inp:
            print_say('OK, back to standby; let me know if you need help!')
            break
        # # Activate the timer
        # elif "timer for" in inp and ("hour" in inp or "minute" in inp):
        #     timer(inp)
        #     continue
        # # Activate the alarm clock
        # elif "alarm for" in inp and ("a.m." in inp or "p.m." in inp):
        #     alarm(inp)
        #     continue
        # # Activate the joke-telling functionality
        elif "joke" in inp:
            joke()
            continue
        elif len(inp) > 10: #to ensure if nothing is said (empty string) voice assistant doesn't call other methods
            ask_wolf()
        elif "email" in inp:
            send_email()
        elif "news" in inp:
            speak_news()
        elif "live radio" in inp:
            live_radio()
        elif "open file" in inp:
            open_file()
        elif "tic tac toe" in inp:
            screen_setup()
        elif "search" in inp:
            search_web()
        elif "search wikipedia" in inp: #don't call funcs within files to not have them run on import
            wiki_search()
        elif "bitcoin watch" in inp:
            bitcoinwatch()
        elif "stock watch" in inp:
            stock_watch()
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