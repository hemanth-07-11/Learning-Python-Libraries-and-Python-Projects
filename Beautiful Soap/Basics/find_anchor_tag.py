#Write a Python program to find the text of the first <a> tag of a given html text.

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;
charset=iso-8859-1">
<title>Hi</title>
</head>
<body>
<h2>HEMANTH N</h2>
<p>
when there are a lot of events possible, the probability of any specific event is very low,virtually zero probablity. But some low probability event is guaranteed to occur.
</p>
<p><a href="https://cricbuzz.com">Check Scores
</a></p>
<p><a href="https://cricbuzz.com">Check Scores
</a></p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')
anchor_tag = soup.find('a').text
print("text of first anchor tag: ", anchor_tag)