import wolframalpha
from constants import print_say

API_KEY = "595KVV-JY64RGJKEG"
wolf = wolframalpha.Client("595KVV-JY64RGJKEG")

while True:
    query = input("What would you like to search?")
    res = wolf.query(query)
    output = next(res.results).text
    print("type", type(output))
    print_say(output)

