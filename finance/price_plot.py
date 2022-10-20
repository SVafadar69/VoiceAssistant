import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import matplotlib.dates as mdates
import datetime
from mysr import voice_to_text
from mysay import print_say

today_date = "2022-10-18"
end_date = datetime.date.today()

print_say("What stock do you want to research")
# inp = voice_to_text()
inp = input()
stock = pdr.get_data_yahoo(inp, start=today_date, end=end_date)

stock['Date'] = stock.index.map(mdates.date2num)

#Choose figure size
fig = plt.figure(dpi=128, figsize=(10, 6))
formatter = mdates.DateFormatter('%m/%d%Y')
plt.gca().xaxis.set_major_formatter(formatter)

plt.plot(stock['Date'], stock['Adj Close'], c="blue")

plt.title(f"The Stock Price of {inp}", fontsize=16)
plt.xlabel('Date', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Price", fontsize=10)
plt.show()