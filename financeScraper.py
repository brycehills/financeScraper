import bs4
import datetime

from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup

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

ticker_table = page_content.findAll("div",{"class":"Ovx(s)"})

for t in ticker_table:

    # attempting to select entire box for an individual company
    ticker_box_white = t.findAll("tr",{"class":"SimpleDataTableRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white) "})
    ticker_box_grey = t.findAll("tr",{"class":"SimpleDataTableRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc($altRowColor) "})

    print("")
    print(len(ticker_box_white))

    print("")
    print(len(ticker_box_grey))

# Timestamp for data purposes
print("\nTime & Date extracted:")
print(current_time)
