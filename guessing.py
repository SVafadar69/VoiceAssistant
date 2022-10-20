import turtle as t
import sys
import os
from random import choice
from tkinter import messagebox
from tkinter import PhotoImage
from mysay import print_say
from mysr import voice_to_text

# Set up the board
t.setup(600,500)
t.hideturtle()
t.tracer(False)
t.bgcolor("lavender")
t.title("Guess the Word Game in Turtle Graphics")
# Define a variable to count how many guesses left
score = 6
# Create a second turtle to show guesses left
left = t.Turtle()
left.up()
left.hideturtle()
left.goto(-290,200)
left.write(f"guesses left:   {score}", font = ('Arial',20,'normal'))
# Put incorrect guesses on top
t.up()
t.goto(-290,150)
t.write("incorrect guesses:", font = ('Arial',20,'normal'))
# Put four empty spaces for the four letters at bottom
for x in range(4):
    t.goto(-275+150*x,-200)
    t.down()
    t.goto(-175+150*x,-200)
    t.up()

with open("chapterSeven/words_file.txt", mode="r+") as words_file:
    words = words_file.readlines()
    print(words)
    # for word in words:
    #     if word == "'" or word == ",":
    #         words = words.replace(word, '')
    #
    # words = words.split()
    # for word in words:
    #     words_file.writelines(f"{word}\n")

    #random word can be declared in open scope

word = choice(words)
coin = PhotoImage(file="cash.png").subsample(10,10) #returns newly formed image based off dimensions
t.addshape("coin", t.Shape("image", coin)) #adding image to turtle

missed = []
# Putting 6 coin images on the screen
coins = [0]*6

for i in range(6):
    coins[i] = t.Turtle('coin')
    coins[i].up()
    coins[i].goto(-100+50*i,0)
t.update()
#
# Prepare the validinputs and gotright lists
validinputs = list('abcdefghijklmnopqrstuvwxyz') #26 items - each letter of alphabet
gotright = []
print_say(f"The word is {word}")

while True:

    print_say("What is your letter guess?")
    # inp = voice_to_text().lower()
    inp = input("Enter a letter to guess")
    print_say(f"You guessed {inp}")
    inp = inp.replace('letter ', '') #replacing spoken "letter" word with ''

    if "stop" in inp:
        print_say("Okay! Ending the application.")
        break
    elif inp not in validinputs:
        print_say("That is not a letter of the alphabet. Please choose a letter")
    else:
        if inp in list(word): #converting word into separate char strings using list() method(?). If word = choice,
            # list(choice) == c h o i c e
            # If yes, put it in the right position(s)
            for w in range(4): #4 lines for the letters
                if inp == list(word)[w]: #if inp = one of the index letters of the word (word: w=0, o=1 etc.)
                    t.goto(-250 + 150 * w, -190) #place that letter on the screen
                    t.write(inp, font=('Arial', 60, 'normal')) #write letter with that font
                    gotright.append(inp)
#
            if len(gotright) == 4:
                print_say("Great job, you got the word right!")
                messagebox.showinfo \
                    ("Game over! You won.")
                break
#
        else:
            score -= 1
            # validinputs.remove(inp)
            coins[-(6 - score)].hideturtle() #as it is a method, remove the amount
            # Update the number of guesses left on board
            left.clear()
            left.write \
                (f"guesses left:   {score}", font=('Arial', 20, 'normal'))
            t.update()
            missed.append(inp)
            t.goto(-290 + 80 * len(missed), 60)
            t.write(inp, font=('Arial', 60, 'normal'))
            if score == 0: #if 6 missed numbers/if score == 0
                # If all six changes are used up, end game
                print_say("You used up all your six guesses!")
                break
                sys.exit
        #validinputs.remove(inp) #removing
    # Update everything that happens in the iteration
    t.update()
t.done()
try:
    t.bye()
except t.Terminator:
    print('exit turtle')
