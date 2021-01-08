#Write a Python program to print the names of all HTML tags of a given web page going through the document tree.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org/").text
soup = BeautifulSoup(page, "lxml")
unique_tags = set()
for tag in soup.find_all(True):
    unique_tags.add(tag.name)

print(unique_tags)