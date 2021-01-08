#  Write a Python program to extract all the text from a given web page.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text

soup = BeautifulSoup(page, 'lxml')
print(soup.get_text())
