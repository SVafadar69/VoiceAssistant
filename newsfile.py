from talkback import *
import pathlib

myfile = pathlib.Path.cwd()/'example.txt' #cwd code will return entire working directory, excluding specific files.

with open(myfile, 'r') as file:
    content = file.read()

    print_say(content)