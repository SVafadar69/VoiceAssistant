from talkback import *

print_say("What is the area of a rectangle?")
inp2 = voice_to_text()
print_say("What is the area of a triangle?")

print(inp, inp2)

area = float(inp) * float(inp2)
print_say(f"The total area is {area}")