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

# print(page_content.head)

# attempting to grab entire table
table = page_content.findAll("div",{"id":"fin-scr-res-table"})

# Timestamp for data purposes
print("\nTime & Date extracted:")
print(current_time)

print(table)
print(len(table))
