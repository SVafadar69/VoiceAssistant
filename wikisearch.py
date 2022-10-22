import wikipedia
from constants import voice_to_text
from constants  import print_say
# inp = voice_to_text()
# my_query = inp("What do you want to know \n").lower()
def wiki_search():
    print_say("Tell me what to look up on Wikipedia")
    my_query = voice_to_text()
    # my_query = "Biography of Elon Musk"
    print_say(f"You said {my_query}")

    answer = wikipedia.summary(my_query)[:200] #limit amount of chars -> 200

    print_say(answer)