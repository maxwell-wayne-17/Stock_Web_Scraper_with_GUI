import requests
from bs4 import BeautifulSoup
from pip._vendor.distlib.compat import raw_input
import PySimpleGUI as sg
import os.path

ongoing = True

while ongoing:

    stockSymbol = raw_input("\nWhat stock value would you like to see?\n")
    URL = 'https://finance.yahoo.com/quote/' + stockSymbol + '?p=' + stockSymbol
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
    print(results + '\n')

    check = raw_input("Would you like to look up another price? (yes/no)\n")
    if check.lower() == 'no':
        ongoing = False

