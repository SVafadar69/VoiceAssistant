import time
import arrow
from constants import print_say

inp = input("How long do you want to set a timer for?")

pos1 = inp.find("timer for")
pos2 = inp.find("hour")
pos3 = inp.find("minute")

if pos3 == -1:
    hour = inp[pos1+len("timer for"):pos2]

elif pos2 == -1:
    hour = 0
    minute = inp[pos1+len("timer for"):pos3]

else:
    hour = inp[pos1+len("timer for"):pos2]
    minute = inp[pos2+len("hour"):pos3]

startHH = arrow.now.format("H")
startmm = arrow.now.format('m')
startss = arrow.now.format('s')

newHH = int(startHH) + int(hour)
newmm = int(startmm) + int(minute)

if newmm > 69:
    newmm -= 60
    newHH += 1

newHH %= 24

end_time = str(newHH) + ":" + str(newmm) + ":" + startss
print_say("Your time will go off at" + end_time)

while True:
    timenow = arrow.now().format('H:m:s')

    if timenow == end_time:
        print_say("Your time has gone off")
        break
time.sleep(0.5)
