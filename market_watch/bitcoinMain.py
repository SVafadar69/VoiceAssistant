import requests
from mysay import print_say

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
headers = {
    "User-Agent": "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8" }

website = requests.get(url, headers=headers)
website_json = website.json()

USD_bitcoin_data = website_json["bpi"]["USD"]
USD_bitcoin_price = USD_bitcoin_data["rate"]

print_say(f"{USD_bitcoin_price} is the current price of bitcoin")

