import openai
import os
from constants import voice_to_text

def dalle(inp):
    inp = voice_to_text()
    openai.Image.create(
        prompt = inp.lower(),
        #number of images to generates
        n = 1
    )

if __name__ == "__main__":
    dalle()