from bs4 import BeautifulSoup
import requests

page_html = requests.get("http://www.coreyms.com").text


soup = BeautifulSoup(page_html, 'lxml')


for article in soup.find_all('article'):

    headline = article.find('h2').text
    print(headline)

    link = article.find('a')["href"]
    print(link)

    paragraph = article.find('div', class_='entry-content').text
    print(paragraph)

    meta_data = article.find('p').text
    print(meta_data)

    embed_vid_link = article.find('iframe', class_='youtube-player')
    if embed_vid_link is not None:
        print(embed_vid_link['src'])

    print("\n")

    