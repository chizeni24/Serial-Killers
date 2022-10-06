import pandas as pd
import requests as rq
from bs4 import BeautifulSoup


## Download the content from the website

url = "https://en.wikipedia.org/wikiList_of_serial_killers_in_the_United_States"
page_request = rq.get(url)

soup = BeautifulSoup(page_request.text, 'html.parser')

print(soup.findAll('table'))