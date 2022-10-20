from yahoo_fin import stock_info as si
from mysay import print_say
import requests, time
from mysr import voice_to_text
from AdvancedVPA import ask_wolf

stock_website = "https://query1.finance.yahoo.com/v1/finance/search?q="

headers = {
    "User-Agent": "Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
def get_stock_info():
    while True:
        print_say("What stock do you want to look for?")
        ticker = str(input("Enter a stock name"))
        # ticker = voice_to_text().lower()
        company = stock_website + ticker
        print(company)

        try:
            response = requests.get(company + ticker, headers=headers)  # adding ticker name to query at end of URL.
            # if 403 error thrown in get attempt, include browser headers
            stock_data = response.json()
            print(stock_data)

            price = float(si.get_live_price(ticker))  # returns the live price of the stocks
            print_say(f"The stock price is {price}")

            stock_ticker = stock_data["quotes"][0]["symbol"]
            print(stock_ticker)

            time.sleep(2)
            # Get other stock related functions from wolfram alpha
            print_say("Do you need anything else from this stock")

            inp = voice_to_text().lower()

            if "no" not in inp:
                ask_wolf()
            if "want to look for a stock" in inp:
                continue  # go back to top of function
            else:
                break
        except:  # throwing exceptions to all exceptions
            pass

if __name__ == "__main__": #code will run while executed in file, but not while imported
    get_stock_info()



