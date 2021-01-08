#Write a Python program to retrieve children of the html tag from a given web page.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org/").text
soup = BeautifulSoup(page, 'lxml')

root = soup.html

root_child = [e.name for e in root.children if e.name is not None]

print(root_child)