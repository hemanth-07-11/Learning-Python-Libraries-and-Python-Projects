import requests
import html
r=requests.get('http://cricapi.com/api/cricket/nKTZgveDZ6WM33uldTtpSmFEZ4i2')
if r.status_code==200:
    curr=r.json()["data"]
    for match in curr:
        print (html.escape(match['title']))

else:
    print ("error")
