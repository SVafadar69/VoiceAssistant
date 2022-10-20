"""To do:
-Organize Code to handle multiple if/elifs efficiently"""

import os, pathlib, platform
import speech_recognition as sr
speech = sr.Recognizer()

my_folder = pathlib.Path.cwd() #path to current working directory (Virtual Assistant Project). Good
#to use if you want to keep all project files stored in one folder - if not need to use dynamic file paths.
print(my_folder)

file_path = r'C:\Users\User\Downloads'
# myfile = my_folder/r'C:\Users\User\PycharmProjects\pythonProject\VirtualAssistant'/'example.txt' #file path

# if platform.system() == "Windows":
#     os.system(f"explorer {myfile}")
#
# elif platform.system() == "Darwin":
#     os.system(f"open {myfile}")
#
# else:
#     os.system(f"xdg-open {myfile}")

def voice_to_text():
    voice_input = ""

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)

        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)

        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
            pass
    return voice_input

def open_file(filename):
    if platform.system() == "Windows":
        # os.system(f"explorer {my_folder}\\{file_path}\\{filename}")
        os.system(f"explorer {file_path}\{filename}")
    elif platform.system() == "Darwin":
        os.system(f"explorer {my_folder}/files/{filename}")

while True:
    print('Python is listening')

    inp = voice_to_text().lower()
    print(f"You just said {inp}")

    if inp == "stop listening":
        print("Goodbye!")
        break

    elif "open pdf" in inp:
        inp = inp.replace('open pdf ','')
        myfile = f'{inp}.pdf'
        open_file(myfile) #method to open specific pdf
        continue

    elif "open word document" in inp:
        inp = inp.replace('open word document ', '')
        myfile = f'{inp}.docx'
        open_file(myfile)
        continue

    elif "open excel document" in inp:
        inp = inp.replace('open excel document ', '')
        myfile = f'{inp}.xlsx'
        open_file(myfile)
        continue

    elif "open powerpoint" in inp:
        inp = inp.replace('open powerpoint ', '')
        myfile = f'{inp}.pptx'
        open_file(myfile)
        continue

    elif "open mp3" in inp:
        inp = inp.replace('open mp3 ', '')
        myfile = f'{inp}.mp3'
        open_file(myfile)
        continue

