import requests
from bs4 import BeautifulSoup
url = "http://www.cricbuzz.com/cricket-match/live-scores"
res = requests.get(url)
soup = BeautifulSoup(res.content,"lxml")
print("\t\t\t\tWELCOME TO LIVE CRICKET SCORE")
print("\n\n")
#print(soup.find_all("a",{"class":"cb-lv-scrs-well-live"})[0].text)
for item in soup.find_all("a",{"class":"cb-lv-scrs-well-live"}):
 print("\t\t\t"+item.text)	
print("\n\n")