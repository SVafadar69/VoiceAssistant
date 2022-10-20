import os
import random, time
from pygame import mixer
from mysay import print_say
from mysr import voice_to_text

with os.scandir("./mptpkg") as mptpkg_files:
    for file in mptpkg_files:
        print(file.name)


while True:
    print_say("How may I help you?")

    inp = voice_to_text().lower()
    # inp = 'play a edm song'
    print_say(f"You just said {inp}")

    if inp == "stop listening":
        print_say(f"You said {inp}, goodbye!")
        break


    if "play a" in inp and "song" in inp:
        inp = inp.replace('play a ', '')
        inp = inp.replace(' song' , '')

    with os.scandir(f'./mptpkg/{inp}') as entries: #moving to genre folder - inp will be genre
        mysongs = [entry.name for entry in entries] #creating list of songs from song names in genre folder
        mysong = random.choice(mysongs) #choosing one song from list


    # #playing specific artist's song
    # names = inp.split()
    # first_name = names[0]
    #
    # if len(names) > 1:
    #     last_name = names[1]
    # else:
    #     last_name = first_name
    #
    # my_songs = []
    #
    # with os.scandir("./mptpkg") as files:
    #     for file in files:
    #         if (first_name in file.name or last_name in file.name) and "mp3" in file.name:
    #             my_songs.append(file.name)
    #
    #     my_song = random.choice(my_songs)
    #     print_say(f"Playing the song {my_song}")
    #     time.sleep(2)
    #     mixer.init()
    #     mixer.music.load(f'./mptpkg/{my_song}')
    #     print("b")
    #     mixer.music.play()

        my_song = random.choice(mysong)
        print_say(f"Playing the song {mysong}")
        time.sleep(2)
        mixer.init()
        mixer.music.load(f'./mptpkg/{inp}/{mysong}') #load folder + inp (name of subfolder) + song name
        print("b")
        mixer.music.play()

        time.sleep(3)
