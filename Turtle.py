"""
Change computer's circle to its color
Randomly choose colour, but still have blue go first
"""

import turtle as t
from random import choice
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr

try:
    engine = pyttsx3.init()
except(ImportError, RuntimeError):
    pass
speech = sr.Recognizer()

def voice_to_text():
    voice_input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input

def print_say(txt):
    print(txt) #printing the spoken word
    engine.say(txt)
    engine.runAndWait()

# Setting up the screen
def screen_setup():
    global occupied, turn, validinputs, rounds, cellcenter
    t.setup(600, 600, 10, 70)
    t.tracer(False)
    t.hideturtle()
    t.bgcolor("red")
    t.title("Tic-Tac-Toe in Turtle Graphics")
    # Draw horizontal lines and vertical lines to form grid
    t.pensize(5)
    for i in (-100, 100):
        t.up()
        t.goto(i, -300)
        t.down()
        t.goto(i, 300)
        t.up()
        t.goto(-300, i)
        t.down()
        t.goto(300, i)
        t.up()
    # Create a dictionary to map cell number to the cell center coordinates - coordinates for x,o
    cellcenter = {'1': (-200, -200), '2': (0, -200), '3': (200, -200),
                  '4': (-200, 0), '5': (0, 0), '6': (200, 0),
                  '7': (-200, 200), '8': (0, 200), '9': (200, 200)}
    # Go to the center of each cell, write down the cell number
    for cell, center in list(cellcenter.items()): #cell = dict key index, center = tuple of x,y coordinates
        t.goto(center)
        t.write(cell, font=('Arial', 20, 'normal'))
    # The blue player moves first
    turn = "blue"
    # Count how many rounds played
    rounds = 1
    # Create a list of valid moves
    validinputs = list(cellcenter.keys())
    # Create a dictionary of moves made by each player
    occupied = {"blue": [], "white": []}

screen_setup()
# Determine if a player has won the game
def win_game(): #if conditions are within list - call game over
    global turn
    win = ['1' in occupied[turn] and '2' in occupied[turn] and '3' in occupied[turn],
           '4' in occupied[turn] and '5' in occupied[turn] and '6' in occupied[turn],
           '7' in occupied[turn] and '8' in occupied[turn] and '9' in occupied[turn],
           '1' in occupied[turn] and '4' in occupied[turn] and '7' in occupied[turn],
           '2' in occupied[turn] and '5' in occupied[turn] and '8' in occupied[turn],
           '3' in occupied[turn] and '6' in occupied[turn] and '9' in occupied[turn],
           '1' in occupied[turn] and '5' in occupied[turn] and '9' in occupied[turn],
           '3' in occupied[turn] and '5' in occupied[turn] and '7' in occupied[turn]]

    if any(win):
        print(turn, "has won")
        return True
#
# Add a dictionary of words to replace
to_replace = {'number ': '', 'cell ': '',
              'one': '1', 'two': '2', 'three': '3',
              'four': '4', 'for': '4', 'five': '5',
              'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
# Start an infinite loop to take voice inputs
while True:
    # Ask for your move
    print_say(f"Player {turn}, what's your move?")
    # Capture your voice input
    # inp = voice_to_text()
    inp = input("Choose a move")
    print_say(f"You said {inp}.")
    for x in list(to_replace.keys()):
        inp = inp.replace(x, to_replace[x]) #replace potential string version of 1 (one) with numerical value 1.
        #would be using keys to occupy spaces then

    if inp in occupied[turn]: #if your move is stored in your turn color's list
        print_say("You already chose that turn")
    elif inp in validinputs:
        # Go to the corresponding cell and place a dot of the player's color
        t.up()
        t.goto(cellcenter[inp])
        t.dot(180, turn)
        t.update()
        # Add the move to the occupied list for the player
        occupied[turn].append(inp) #adding to occupied moves
         # Disallow the move in future rounds
        validinputs.remove(inp) #remove from board
         # check if the player has won the game
        if win_game(): #if function returns true - test both iterations of true
             # if a player wins, invalid all moves, end the game
            validinputs = []
            print_say(f"Congrats player {turn}, you won!")
            messagebox.showinfo \
                ("End Game", f"Congrats player {turn}, you won!")

            if turn == "blue":
                turn = "white"
            else:
                turn = "blue"
            break
         # If all cellls are occupied and no winner, it's a tie
        elif rounds == 9:
            print_say("Game over, it's a tie!")
            messagebox.showinfo("Tie Game", "Game over, it's a tie!")
            break
         # Counting rounds
        rounds += 1

        # The computer makes a random move
        comp_inp = choice(validinputs)
        print_say(f'The computer occupies cell {comp_inp}.')
        t.up()
        t.goto(cellcenter[comp_inp])
        t.dot(180, turn)
        t.update()
        occupied[turn].append(comp_inp)
        validinputs.remove(comp_inp)

    else:
        print_say("Sorry, that's an invalid move!")

t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')

