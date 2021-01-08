# Write a Python program to retrieve all the paragraph tags from a given html document. 
from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>Some Random Page</title>
</head>
<body>
<h2>Some Random heading</h2>
<p>when there are a lot of events possible, the probability of any specific event is very low,virtually zero probablity. But some low probability event is guaranteed to occur.
</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
paragraphs = soup.find_all('p')
print(paragraphs)