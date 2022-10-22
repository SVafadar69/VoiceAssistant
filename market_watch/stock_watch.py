import tkinter as tk

import arrow
from yahoo_fin import stock_info as si

from constants import print_say

# Create a root window hold all widgets
root = tk.Tk()
# Specify the title and size of the root window
root.title("U.S. Stock Market Watch")
root.geometry("1100x750")
# Create a first label using hte Label() function
label = tk.Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# Create a second label
label2 = tk.Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()
# Set up tickers and names
tickers = ['^DJI', '^GSPC', 'AAPL', 'AMZN', 'TSLA']
names = ['DOW JONES', 'S&P500', 'Apple', 'Amazon', 'Tesla']
# Set up the oldprice values and price bounds

old_price = []
max_price = []
min_price= []
m = []
a = []

for i in range(len(names)):
    p = round(float(si.get_live_price(tickers[i])), 2) #get price of each stock ticker, to the 2nd decimal
    old_price.append(p)
    max_price.append(p*1.1)
    min_price.append(p*0.9)
    print_say(f'The latest stock price for {names[i]} is {p} dollars') #get latest price of each ticker from live_price api

def stock_watch():
    global old_price, max_price, min_price
    for i in range(len(tickers)):
        #a.append(round(float(si.get_live_price(tickers[i])), 2)) #appending float to list
        a.insert(i, round(float(si.get_live_price(tickers[i])), 2)) #inserting at each element of i
        m.append(f"{names[i]}: {a[i]}")

    tdate = arrow.now().format('MMMM DD, YYYY')
    tm = arrow.now().format('hh:mm:ss A')
    # Put the date and time information in the first label
    label.configure(text=tdate + "\n" + tm)
    # Put all the five messages on the stock market in the second label
    label2.configure(text=m[0] + \
                          "\n" + m[1] + "\n" + m[2] + "\n" + m[3] + "\n" + m[4], justify=tk.LEFT)
    #If there is update in the marekt, announce it
    for i in range(len(a)):
        if a[i] != old_price[i]: #if price in list does not equal old price,
            old_price[i] = a[i]
            print_say(f'The latest stock price for {names[i]} is {p[i]} dollars!')
            # if price goes out of bounds, announce it
        if a[i] > max_price[i]:
            print_say(f'{names[i]} has increased by 10%!')
            max_price[i] = a[i] #new highest price was assigned to highest a[i]
        if a[i] < min_price[i]:
            print_say(f'{names[i]} has decreased by 10%!')
            min_price[i] = a[i] #new lowest price has been assigned
            # Call the stock_watch() function
    root.after(120000, stock_watch) #call the function every 2 minutes.
# Run the game loop
stock_watch() #call function once
root.mainloop()
