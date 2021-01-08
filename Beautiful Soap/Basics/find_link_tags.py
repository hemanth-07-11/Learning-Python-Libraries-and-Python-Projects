# Write a Python program to find all the link tags and list the first ten from the webpage python.org.

from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text
soup = BeautifulSoup(page, 'lxml')
anchor_tags = soup.find_all('a')
print(anchor_tags[0:10])