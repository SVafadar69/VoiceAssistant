from constants import print_say
from constants import time
from constants import voice_to_text
import requests
import bs4


def speak_news():
    print_say("Here's an overview of what's going on today")
    res = requests.get('https://www.npr.org/sections/news/')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    div_tags = soup.find_all('div', class_='item-info')
    print(div_tags[1])

    news_index = 1

    #div_tags, news_index = scrape_news() #assigning return function of scraping_website to div_tags, and news_index

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
        if news_index > 3:
            break



def play_news():

    print_say("Would you like me to play some of today's news?") #positive responses - yes, sure, why not, etc.

    inp = voice_to_text()
    if "yes" in inp:
        time.sleep(2)
        speak_news()

play_news()
