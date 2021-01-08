#  Write a Python program to retrieve the HTML code of the title, its text, and the HTML code of its parent.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text 
soup = BeautifulSoup(page, 'lxml')

print(soup.title)
print(soup.title.text)
print(soup.title.parent)