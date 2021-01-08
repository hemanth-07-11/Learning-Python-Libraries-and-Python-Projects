# Write a Python program to find all the h2 tags and list the first four from the webpage python.org.
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.python.org").text
soup = BeautifulSoup(page, 'lxml')
headlines = soup.find_all('h2')[0:4]
print(headlines)