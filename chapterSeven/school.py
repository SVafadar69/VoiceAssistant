# from constants import print_say
# import webbrowser
#
# stevens_entries = {}
# inp = voice_to_text().lower()
# inp = inp.replace('')
# webbrowser.open("http://google.com/search?q=" + inp)  # -> URL for google queries

import openai
from constants import voice_to_text, print_say

openai.api_key = "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"
#inp = voice_to_text()
name = "Steven"

def conversation():

    while True:

        inp = str(input())

        if "stop" in inp:
            print_say("Okay, exiting the program")
            return False

        print("user input", inp)

        response = openai.Completion.create(engine='text-davinci-001', prompt=inp, max_tokens=50)  # prompt gets created into dict.
        bot_response = response["choices"][0]["text"].replace('"', '') #retrieve the response with text index.replacing string quotes
        print("bot response", bot_response)
        print(type(bot_response))
        print_say(bot_response)

#conversation(user_response=voice_to_text())
conversation()

# bot_response = response["choices"][0]["text"].replace('\n', "")
# response_split = bot_response.split(name + ": ", 1)[0].split("Bot: ", 1)[
#     0]  # split string on name + :. max split = 1 -> runs split once.
# # returns first string with [0], resplits on bot, returns first string return after that split.

if __name__ == "__main__":
    conversation()