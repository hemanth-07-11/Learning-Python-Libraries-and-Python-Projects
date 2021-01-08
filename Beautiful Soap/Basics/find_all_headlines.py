#  Write a Python program to a list of all the h1, h2, h3 tags from the webpage python.org.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text
soup = BeautifulSoup(page, "lxml")

print("List of all the h1, h2, h3 headings: ")

for headline in soup.find_all(['h1', 'h2', 'h3']):
    print(headline.name + " " + headline.text.strip())