# from constants import print_say
# import webbrowser
#
# stevens_entries = {}
# inp = voice_to_text().lower()
# inp = inp.replace('')
# webbrowser.open("http://google.com/search?q=" + inp)  # -> URL for google queries

import openai
import os
from constants import voice_to_text, print_say
from constants import api_key
from imageDally import dalle, chatGPT


openai.api_key = api_key
name = "Steven"

def conversation():
    #print_say("What do you want to talk about")
    while True:
        #inp = voice_to_text()

        inp = str(input("Waiting for your input")).lower()

        if "stop" in inp:
            print_say("Okay, exiting the program")
            return

        elif "dalle" in inp:
            dalle()

        elif "chatgpt" in inp:
            chatGPT()

        else:

            #GPT3 incorporation

            response = openai.Completion.create(engine='text-davinci-001', prompt=inp, max_tokens=50)  # prompt gets created into dict.
            bot_response = response["choices"][0]["text"].split('. ')
            bot_response = [bot_response.split('\n')[-1] for bot_response in bot_response[:2]] #slicing list to 2, taking the 2nd
            #index of bot response split that does not contain bad characters


            print_say(bot_response)

            print("user input", inp)

        # print("bot response", bot_response)
        # print(type(bot_response))


#conversation(user_response=voice_to_text())

# bot_response = response["choices"][0]["text"].replace('\n', "")
# response_split = bot_response.split(name + ": ", 1)[0].split("Bot: ", 1)[
#     0]  # split string on name + :. max split = 1 -> runs split once.
# # returns first string with [0], resplits on bot, returns first string return after that split.

if __name__ == "__main__":
    conversation()
    #dalle() doesn't need 2nd declaration of func if already getting imported and used.
    openai.api_key
