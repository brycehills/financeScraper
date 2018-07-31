#import libraries
import bs4
import datetime

from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup

# create time vairable
current_time = datetime.datetime.now()

# variable to make url more readbale
link = 'https://finance.yahoo.com/cryptocurrencies'

# vARIABLE = REQUEST FROM URL
uClient = request(link)

# varibale to store everything pulled from page
page_html = uClient.read()
# close page
uClient.close()

# html parsing
page_content = soup(page_html, "html.parser")

# Timestamp for data purposes
print("\n****************************")
print("Time & Date extracted:")
print(current_time)
print("****************************\n")

ticker_column_white = page_content.findAll("tr",{"class":"SimpleDataTableRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white) "})
ticker_column_grey = page_content.findAll("tr",{"class":"SimpleDataTableRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc($altRowColor) "})

for t in ticker_column_white:

    symbol_w = t.a.text
    print("SYMBOL:          " + symbol_w)

    # NAME
    ticker_name_w = t.img["alt"]
    print("NAME:            " + ticker_name_w)

    # PRICE
    price_w = t.span.text
    print("PRICE:           $" + price_w)

    # change in stock
    changeContainer_w = t.findAll("td",{"aria-label":"Change"})
    change_w = changeContainer_w[0].text
    print("CHANGE:          " + change_w)

    # 24hr change in stock
    percent_changeContainer_w = t.findAll("td",{"aria-label":"% Change"})
    percent_change_w = percent_changeContainer_w[0].text
    print("PERCENT CHANGE:  " + percent_change_w)

    # print newline to separate company
    print("")

print("-------------------------------------------------")

for t in ticker_column_grey:

    symbol_g = t.a.text
    print("SYMBOL:           " + symbol_g)

    # name
    ticker_name_g = t.img["alt"]
    print("NAME:             " + ticker_name_g)

    # PRICE
    price_g = t.span.text
    print("PRICE:            $" + price_g)

    # change in stock
    changeContainer_g = t.findAll("td",{"aria-label":"Change"})
    change_g = changeContainer_g[0].text
    print("CHANGE:           " + change_g)

    # 24hr change in stock
    percent_changeContainer_g = t.findAll("td",{"aria-label":"% Change"})
    percent_change_g = percent_changeContainer_g[0].text
    print("PERCENT CHANGE:   " + percent_change_g)

    # print newline to separate company
    print("")
