'''
Author: Steven Vafadar,
Last Modified: Ken Tao Zheng
Date: Dec 6th 2022
'''

import wolframalpha
import time

from constants import wikipedia
from constants import voice_to_text
from constants import print_say
from constants import wolf, API_KEY
import webbrowser

'''
This file is used to access the Wolfram Alpha Scientific Search Engine. It is primarily used for scientific queries outside the realm
of typical GPT-3 queries. It leverages Wolfram Alpha, which is the greatest scientific search engine in the world, to make the scientific
query process more efficient. 
'''

def ask_wolf():
    while True:
        print_say("What do you want to look up?")
        inp = voice_to_text().lower()
        print(inp)

        if "stop" in inp: #dynamic set of words applicable to numerous functions to turn off
            print_say("Okay, turning off.")
            break

        time.sleep(2)
        response = wolf.query(inp)

        #retrieve the text from response
        try:
            res = next(response.results).text #retrieve text result of Query
            print_say(res) #read out loud text

        #Using wikipedia if Wolfram Alpha Fails
        except Exception as e:
            try:
                print_say("This is taken from Wikipedia")
                answer = wikipedia.summary(inp)
                print_say(answer[:200])
            except Exception as e:
                repeat_exception(e)
                try:
                    print_say("This is taken from Google")
                    answer = wikipedia.summary(inp)
                    print_say(answer[:200])
                except Exception as e:
                    repeat_exception(e)
                try:
                    print_say("I couldn't find your request online. Opening google for you.")
                    webbrowser.open("http://google.com/search?q=" + inp)  # -> URL for google queries
                except Exception as e:
                    repeat_exception(e)
                pass

        #else: #will execute if no exception

        #finally: #will execute no matter what

#call out the function error
def repeat_exception(e):
    print_say(f"I could not find that answer. You got an error of {type(e).__name__} while I was looking up your query.")
    # returns type of PageError
    print_say(repr(e))

if __name__ == "__main__":
    ask_wolf()
    # repeat_exception(e=e)

