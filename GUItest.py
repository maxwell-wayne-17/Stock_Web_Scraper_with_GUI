import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

# Function to scrape yahoo finance and get stock price from a given symbol
def getStockPrice(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text

    return price


# Create GUI Layout
layout = [
    # Message above text box
    [sg.Text('Please enter a stock symbol')],

    # Create text box for user
    [
        sg.Text("Stock Symbol"),
        sg.In(size=(15, 1), enable_events=True, key="-SYMBOL-")
    ],

    # Create area to display stock symbols and prices
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-STOCKS LIST-"
        )
    ],

    # Submit and cancel buttons
    [sg.Submit(), sg.Cancel()]
]

# Open the labeled window with layout above
window = sg.Window('Yahoo Stock Scraper', layout)

stockSymbols = []
stockPrices = []
# Array to hold stock symbol and prices
displayLines = []
# Used to help format text
emptyStr = ""

while True:

    event, values = window.read()

    # Event was cancel button or close window
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break

    # Event was enter in stock symbol text box
    if event == "-SYMBOL-":
        stock = values["-SYMBOL-"]

    # Event was submit button clicked or enter
    if event == "Submit":
        # Add current text in box to array
        stockSymbols.append([stock])

        # Get stock price
        results = getStockPrice(stock)
        stockPrices.append([results])

        # Add symbol and price to the display array
        lastIndex = len(stockSymbols) - 1
        line = f"{emptyStr.join(stockSymbols[lastIndex])} ${emptyStr.join(stockPrices[lastIndex])}"
        displayLines.append(line)

        # Display the array
        window["-STOCKS LIST-"].update(displayLines)

window.close()
