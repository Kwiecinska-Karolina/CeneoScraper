import requests
from bs4 import BeautifulSoup


url = "https://www.ceneo.pl/95365253#tab=reviews"
response = requests.get(url)

page_dom = BeautifulSoup(response.text, 'html.parser')

# print(page_dom.prettify())

#user-post__author_name
autor = page_dom.find_all("span", {"class": "user-post__author-name"})

print(autor)
