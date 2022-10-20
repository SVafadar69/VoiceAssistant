import wolframalpha
import wikipedia
import time

from mysr import voice_to_text
from mysay import print_say
API_KEY = "595KVV-JY64RGJKEG"
wolf = wolframalpha.Client("595KVV-JY64RGJKEG")
def ask_wolf():
    while True:
        print_say("What do you want to say?")
        inp = voice_to_text().lower()
        print(inp)

        if inp == "stop":
            print_say("Okay, turning off.")
            break

        time.sleep(2)
        response = wolf.query(inp)

        #retrieve the text from response
        try:
            res = next(response.results).text #retrieve text result of Query
            print_say(res) #read out loud text
        except:
            try:
                print_say("This is taken from Wikipedia")
                answer = wikipedia.summary(inp)
                print_say(answer[:200])
            except:
                print_say("I could not find that answer. Download the google module and retrieve the text response.")
        finally:
            try:
                print_say("This is taken from Wikipedia")
                answer = wikipedia.summary(inp)
                print_say(answer[:200])
            except:
                print_say("I could not find that answer. Something is most likely wrong with the APIs or your code.")


if __name__ == "__main__":
    ask_wolf()