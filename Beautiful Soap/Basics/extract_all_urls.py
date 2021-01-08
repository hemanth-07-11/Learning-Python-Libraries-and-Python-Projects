# Write a Python program to extract all the URLs from the webpage python.org that are nested within <li> tags from .

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text
soup = BeautifulSoup(page, 'lxml')


count = 0
for element in soup.find_all('li'):
    count += 1
    anchor_tag = element.find('a')
    print("Page link: " + str(count), anchor_tag["href"])