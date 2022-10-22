from constants import wikipedia
from constants import voice_to_text
from constants import print_say
import traceback

def wiki_search():

        print_say("Tell me what to look up on Wikipedia")
        my_query = voice_to_text()
        print_say(f"Looking up {my_query}")

        try:
            answer = wikipedia.summary(my_query)[:200] #limit amount of chars -> 200
            print_say(answer)

        except wikipedia.exceptions.PageError:
            exception = traceback.print_exception()
            print_say(exception)

wiki_search()