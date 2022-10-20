import requests
import bs4
import time
from mysay import print_say
from mysr import voice_to_text


def scraping_website():
    res = requests.get('https://www.npr.org/sections/news/')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # global div_tags
    # global news_index
    div_tags = soup.find_all('div', class_='item-info')
    news_index = 1

    return div_tags, news_index

def speak_news():

    div_tags, news_index = scraping_website() #assigning return function of scraping_website to div_tags, and news_index

    #global div_tags, news_index #to use previous global vars in other function, must declare lobal twice.

    for div_tag in div_tags:
        print_say(f"News Article # {news_index}")
        # Retrieve and print the h2 tag that contains the title
        h2tag = div_tag.find('h2', class_="title")
        print_say(h2tag.text)
        # Retrieve and print the p tag that contains the teaser
        ptag = div_tag.find('p', class_="teaser")
        print_say(ptag.text)

        # Moving through the first 10 news articles
        news_index += 1
        if news_index > 10:
            break


print_say("Would you like me to play some news articles?")

input = voice_to_text().lower()

if input == "yes":
    time.sleep(2)
    speak_news()


