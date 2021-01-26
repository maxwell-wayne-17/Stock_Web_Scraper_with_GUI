import requests
from bs4 import BeautifulSoup
from pip._vendor.distlib.compat import raw_input


def getStockPrice(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}?p={symbol}'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    except AttributeError:
        return -1

    return price


ongoing = True

while ongoing:

    stockSymbol = raw_input("\nWhat stock value would you like to see?\n")
    results = getStockPrice(stockSymbol)
    if results != -1:
        print(results + '\n')
    else:
        print('Invalid stock symbol')

    check = raw_input("Would you like to look up another price? (yes/no)\n")
    if check.lower() == 'no':
        ongoing = False
