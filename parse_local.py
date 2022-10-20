import bs4
from bs4 import BeautifulSoup
from io import BytesIO
from pygame import mixer
import requests
import webbrowser
from mysay import print_say
from mysr import voice_to_text
import sys

def news_brief():

    website = 'https://www.npr.org/podcasts/500005/npr-news-now/'

    response = requests.get(website)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    #Locating mp3 files
    casts = soup.find_all('a', {'class': 'audio-module-listen'})
    # print(casts)

    cast = casts[0]["href"]
    print("link", cast)
    post = cast.find('?')
    # post = cast.partition('?')

    #returns everything not including last element - getting URL of MP3
    mp3_file = cast[:post]
    #snipping link up to question mark
    #webbrowser.open(mp3_file) #open the file in the using webbrowser method

    my_mp3 = requests.get(mp3_file)

    voice = BytesIO()
    voice.write(my_mp3.content)
    voice.seek(0)
    mixer.init()
    mixer.music.load(voice)
    mixer.music.play()

    background = voice_to_text().lower()
    stop = stop_music()

while True:
    print_say('Python is listening..')
    inp = voice_to_text().lower()

    print_say(f"You just said {inp}")

    if inp == "stop listening": #replacing with plethora of commands
        print_say("Goodbye!")
        break

    elif "news" in inp:
        news_brief()

def stop_music():

    background = news_brief()
    print_say("Still listening. Let me know if you want me to change the news, or stop.")
    if "stop" in background:
        mixer.music.stop()
        sys.exit

# web_links = []
# for i in range(len(casts)):
#     web_links.append(casts[i]["href"])
# print(web_links)