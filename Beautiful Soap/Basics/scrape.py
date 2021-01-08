from bs4 import BeautifulSoup
import requests

with open('sample.html', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

# returns simple.html without formatting
print(soup)
# returns formatted simple.html
print(soup.prettify())
# returns title along with title tag
match = soup.title
print(match)
# returns title as text without any html tag
title = soup.title.text
print(title)
# returns the first div of the html page
first_div = soup.div
print(first_div)
# find footer of the html page, returns the first div
div_footer_test = soup.find('div')
print(div_footer_test)
# returns all the divs having same class
for article in soup.find_all('div', class_='articles'):
    # article link returns text
    headline = article.h2.a.text
    print(headline)
    # summary
    summary = article.p.text
    print(summary)