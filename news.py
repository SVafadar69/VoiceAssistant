import requests
import bs4

res = requests.get('https://www.npr.org/sections/news/')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

div_tags = soup.find_all('div', class_='item-info')
print(div_tags[1])

news_index = 1

for div_tag in div_tags:
    print(f"News Article # {news_index}")
    # Retrieve and print the h2 tag that contains the title
    h2tag = div_tag.find('h2', class_="title")
    print(h2tag.text)
    # Retrieve and print the p tag that contains the teaser
    ptag = div_tag.find('p', class_="teaser")
    print(ptag.text)

    # Moving through the first 10 news articles
    news_index += 1
    if news_index > 10:
        break