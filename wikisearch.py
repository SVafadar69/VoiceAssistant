from constants import wikipedia
from constants import voice_to_text
from constants import print_say
import traceback

def wiki_search():

    while True:

        print_say("Tell me what to look up on Wikipedia")
        my_query = voice_to_text()
        print_say(f"Looking up {my_query}")

        try:
            answer = wikipedia.summary(my_query)[:200] #limit amount of chars -> 200
            print_say(answer)

        except Exception as e:
            print_say(f"You got an error of {type (e).__name__} while I looking up your query.") #returns type of PageError
            print_say(repr(e))

        print_say("Do you want me to do another query?")

        print("Waiting for your response...")
        inp = voice_to_text()

        if "yes" not in inp:
            break

if __name__ == "__main__":
    wiki_search()
