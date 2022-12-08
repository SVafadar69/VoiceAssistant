# from constants import print_say
# import webbrowser
#
# stevens_entries = {}
# inp = voice_to_text().lower()
# inp = inp.replace('')
# webbrowser.open("http://google.com/search?q=" + inp)  # -> URL for google queries

'''
Author: Steven Vafadar (301171884), Ken Tao Zheng (301070670)
Last Modified: Steven Vafadar
Date: Dec 6th 2022
'''

'''
This is the general file for incorporating all of openAIs different AI modules. This includes ChatGPT, GPT3, and Dall-E. Future 
iterations will include the incorporation of Codex (automated coding) that is functionable through voice input. This module is essentially
created to leverage all of current openAI abilities, to make a programmer more efficient. 
'''

import openai
import os
from constants import voice_to_text, print_say
from constants import api_key
from imageDally import dalle, chatGPT


openai.api_key = api_key
name = "Steven"

#Initating all functions of OpenAI - Dalle, ChatGPT, GPT3

def conversation():
    while True:

        print_say("How can I help you?")
        inp = voice_to_text().lower()


        if "stop" in inp:
            print_say("Okay, exiting the program")
            return

        elif "image generation" in inp:
            dalle()

        elif "gpt" in inp:
            chatGPT()

        #GPT3 incorporation

        else:

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
