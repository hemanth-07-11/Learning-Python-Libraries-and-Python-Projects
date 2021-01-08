import requests,os,bs4,win10toast
from win10toast import  ToastNotifier
url='https://www.cricbuzz.com/cricket-match/live-scores'
import time
toaster =ToastNotifier()
while(True):
	try:	
		
			res=requests.get(url)
			ans=bs4.BeautifulSoup(res.text,"html5lib")
			req=ans.select('.cb-lv-scrs-col')
			req=req[0].getText()
			print(req)
			#print(res.text[1:250])
			toaster.show_toast(str(req))
			time.sleep(100)
	except ConnectionError:
		time.sleep(100)