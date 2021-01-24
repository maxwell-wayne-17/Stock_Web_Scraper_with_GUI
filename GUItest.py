import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup

layout = [
    [sg.Text('Please enter a stock symbol')],
    [
        sg.Text("Stock Symbol"),
        sg.In(size=(15, 1), enable_events=True, key="-SYMBOL-")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40,20), key="-STOCKS LIST-"
        )
    ],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Yahoo Stock Scraper', layout)

stockSymbols = []
stockPrices = []
# Used to help format text
emptyStr = ""
while True:

    event, values = window.read()

    # Event was cancel button or close window
    if event == "Cancel" or event == sg.WIN_CLOSED:
        break

    # Event was enter in stock symbol text box or submit
    if event == "-SYMBOL-":
        stock = values["-SYMBOL-"]

    # Event was submit button clicked or enter
    if event == "Submit":
        # Add current text in box to array
        stockSymbols.append([stock])

        # Search of yahoo finance page of inputted stock and get raw HTML (Split into definition later)
        URL = f'https://finance.yahoo.com/quote/{stock}?p={stock}'
        page = requests.get(URL)

        # Parse HTML
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
        stockPrices.append([results])

        # Wonky way to only add first in array, need to use for loop to update with entire list
        lastIndex = len(stockSymbols) - 1
        line = f"{emptyStr.join(stockSymbols[lastIndex])} ${emptyStr.join(stockPrices[lastIndex])}"
        window["-STOCKS LIST-"].update([line])

window.close()

