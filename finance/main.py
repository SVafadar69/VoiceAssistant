from myplot import price_plot
from mychart import candle_stick
from mysay import print_say
from mysr import voice_to_text

def finance_patterns():
    while True:
        print_say("what can I help you with")
        inp = voice_to_text()

        if "stop listening" in inp:
            print_say("Understood. Turning off")
            break
        elif "price pattern for" in inp:
            pos = inp.find('price pattern for ') #returns index of string
            print(pos)
            firm = inp[pos+len('price pattern for'):] #indexing string from user input (price pattern for :spoken stock word)
            #2nd way of accessing stock name in user input - stock = stock.replace("price pattern for ", '').lower()
            price_plot(firm)
            continue
        elif "chart for" in inp:
            pos = inp.find('chart for ')
            firm = inp[pos+len('chart for '):]
            candle_stick(firm)
            continue
        else:
            pass

finance_patterns()