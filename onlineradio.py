import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from constants import voice_to_text
from constants import print_say


def live_radio():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    CHROMEDRIVER = r"C:\Users\User\Downloads\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER, chrome_options=chrome_options)

    global button
    website = "https://onlineradiobox.com/us/"
    browser.get(website)
    button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/button[3]")
    button.click()

# Start the loop

def play_radio():
    while True:
        print_say("How may I help you?")
        inp = voice_to_text().lower()
        print_say(f'You just said {inp}.')
        if inp == "stop listening":
            print_say('Goodbye!')
            break
        elif "radio" in inp:
            print_say('OK, play live radio online for you!')
            live_radio()
            # Say stop playing to stop the radio any time
            while True:
                background = voice_to_text().lower()
                if "stop playing" in background:
                    button.click() #pauses the radio
                    break
                else:
                    continue

if __name__ == "__main__":
    play_radio()