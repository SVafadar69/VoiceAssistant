import turtle as t
from time import sleep
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
import random

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
    print(txt)  # printing the spoken word
    engine.say(txt)
    engine.runAndWait()

# Set up the screen
t.setup(700, 600)
t.hideturtle()
t.tracer(False)
t.bgcolor("lightgreen")
t.title("Connect Four in Turtle Graphics")
# Draw six thick vertical lines
t.pensize(5)
for i in range(-250, 350, 100):
    t.up()
    t.goto(i, -350)
    t.down()
    t.goto(i, 350)
    t.up()
# Draw five thin gray horizontal lines to form grid
t.pensize(1)
t.pencolor("grey")
for i in range(-200, 300, 100):
    t.up()
    t.goto(-350, i)
    t.down()
    t.goto(350, i)
    t.up()
# Write column numbers on the board
colnum = 1
for x in range(-300, 350, 100):
    t.goto(x, 270)
    t.write(colnum, font=('Arial', 20, 'normal'))
    colnum += 1
# The red player moves first
turn = ["Red", "Blue"]
turn = random.choice(turn)
print(turn)
# The x-coordinates of the center of the 7 columns
xs = [-300, -200, -100, 0, 100, 200, 300]
# The y-coordinates of the center of the 6 rows
ys = [-250, -150, -50, 50, 150, 250]
# Keep track of the occupied cells
occupied = [ [], [], [], [], [], [], ]
# Create a second turtle to show disc falling
fall = t.Turtle()
fall.up()
fall.hideturtle()
# Create a list of valid moves
validinputs = ['1', '2', '3', '4', '5', '6', '7']


# Define all win conditions
def win_conditions(x, y, turn):
    # global win
    for dif in (-3, -2, -1, 0):
        try:
            win = [occupied[x + dif][y] == turn
                   and occupied[x + dif + 1][y] == turn \
                   and occupied[x + dif + 2][y] == turn \
                   and occupied[x + dif + 3][y] == turn \
                   and x + dif >= 0,

                   occupied[x][y] == turn \
                   and occupied[x][y - 1] == turn \
                   and occupied[x][y - 2] == turn \
                   and occupied[x][y - 3] == turn \
                   and y - 3 >= 0,

                   occupied[x + dif][y + dif] == turn
                   and occupied[x + dif + 1][y + dif + 1] == turn \
                   and occupied[x + dif + 2][y + dif + 2] == turn \
                   and occupied[x + dif + 3][y + dif + 3] == turn \
                   and x + dif >= 0 and y + dif >= 0,

                   occupied[x + dif][y - dif] == turn \
                   and occupied[x + dif + 1][y - dif - 1] == turn \
                   and occupied[x + dif + 2][y - dif - 2] == turn \
                   and occupied[x + dif + 3][y - dif - 3] == turn \
                   and x + dif >= 0 and y - dif - 3 >= 0]

            if any(win): #if else is not defined after try + except, any(win) becomes undefined. Can also be defined within the try block.
                win = True
                return win

        except IndexError:
            pass


# # Define a win_game() function to check if someone wins the game
#
def win_game(col, row, turn):
    # Convert column and row numbers to indexes in the list of lists occupied
    x = col - 1
    y = row - 1
    # Check all winning possibilities
    if win_conditions(x, y, turn): #win in win_conditions does not need to be declared globally, because its data is being accessed through each function
        return True

# # Count the number of rounds
rounds = 1
# # Add a dictionary of words to replace
to_replace = {'number ': '', 'cell ': '',
              'one': '1', 'two': '2', 'three': '3',
              'four': '4', 'for': '4', 'five': '5',
              'six': '6', 'seven': '7'}
# # Start an infinite loop to take voice inputs

while True:
    # Ask for your move
    print_say(f"Player {turn} it's your turn")
    # Capture your voice input
    # inp = voice_to_text().lower()
    inp = input("Enter a move?")
    print_say(f"You said {inp}.")
    for x in list(to_replace.keys()):
        inp = inp.replace(x, to_replace[x])
    # if move already taken
    # If col is not a valid move, try again
    if inp not in validinputs:
        print_say("Sorry, that's an invalid move!")
        # If your voice input is a valid column number, play the move
    else:
        col = int(inp)
        # Calculate the lowest available row number in that column
        row = len(occupied[col - 1]) + 1
        # Show the disc fall from the top
        if row < 6:
            for i in range(6, row, -1):
                fall.goto(xs[col - 1], ys[i - 1])
                fall.dot(80, turn)
                t.update()
                sleep(0.05)
                fall.clear()
        # Go to the cell and place a dot of the player's color
        t.up()
        t.goto(xs[col - 1], ys[row - 1])
        t.dot(80, turn)
        t.update()
        # Add the move to the occupied list to keep track
        occupied[col - 1].append(turn)

        #Check if the player has won
        if win_game(col, row, turn):
            print("True")
        #     # If a player wins, invalid all moves, end the game
        #     validinputs = []
        #     print_say(f"Congrats player {turn}, you won!")
        #     messagebox.showinfo("End Game", f"Congrats player {turn}, you won!")
        #     break
        # # If all cellls are occupied and no winner, it's a tie
        # elif rounds == 42:
        #     print_say("Game over, it's a tie!")
        #     messagebox.showinfo("Tie Game", "Game over, it's a tie!")
        #     break
        # # Counting rounds
        # rounds += 1
        # # Update the list of valid moves
        # if len(occupied[col - 1]) == 6:
        #     validinputs.remove(str(col))
        # #     # Give the starting turn to the other player

t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
