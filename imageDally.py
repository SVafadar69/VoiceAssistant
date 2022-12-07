import openai
import os
from constants import voice_to_text, print_say
from constants import api_key
from AdvancedVPA import repeat_exception
from selenium import webdriver
from selenium.webdriver.common import keys
import time

chromedriver = r"C:\Users\User\Downloads\chromedriver.exe"
openai.api_key = "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"

def dalle():
    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.minimize_window()

    while True:
        #inp = voice_to_text()

        print_say("What image would you like me to generate?")
        inp = input("Enter something")

        if "Stop Using Dalle".lower() in inp:
            print_say("Switching back to main mode")
            break

        try:
            image = openai.Image.create(
                prompt = inp.lower(),

                #number of images to generates
                n = 1,

                #size of image
                size = "512x512",

             )

            url = image["data"][0]["url"]

            time.sleep(3)
            driver.get(url)
            driver.maximize_window()

            time.sleep(4)
            driver.minimize_window()

        #General Exception Handling
        except Exception as e:
            repeat_exception(e)
            pass

if __name__ == "__main__":
    dalle()
    #repeat_exception()
    openai.api_key