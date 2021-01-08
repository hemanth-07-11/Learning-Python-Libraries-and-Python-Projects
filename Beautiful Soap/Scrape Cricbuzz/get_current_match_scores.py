import requests
from bs4 import BeautifulSoup
from time import sleep

# live - scores of matches
url = 'http://www.cricbuzz.com/cricket-match/live-scores'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
match_details = soup.select('.cb-mtch-lst')

while True:
    for match_score in match_details:
        print(match_score.find('h3').text)
        try:
            print(match_score.find(class_='cb-lv-scrs-col').text)
        except:
            print('Sorry no data available !')
        print()
    sleep(300)      # again fetch the scores after 5 mins
