#Get title
from bs4 import BeautifulSoup

html_doc = """

 <html>
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <head>
  <title>Some Random Page</title>
    <style>
       h1 {
  	    color: red;
 	    text-align: center;
  	    font-family: courier;
            font-weight: bold;
            padding: 30px;
  	    border: 2px solid red;
            margin: 50px ;
           
           }
         body { background-color: silver;}
      </style>


<body>

<h1>  <font size="100" color="blue" > <b> HEMANTH </b> </font> </h1>

<audio controls>
  
  <source src="ex.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio>
<embed src="https://images.indianexpress.com/2019/09/virat-kohli-test-759.jpg">
<br>
<iframe width="420" height="315"
src="https://www.youtube.com/embed/Ib1yzG4A8rg?autoplay=1">
</iframe>
<center>
<iframe width="420" height="315"
src="https://www.youtube.com/embed/TvrbUDfA7KM?controls=0">
</iframe>
</center>
</body>
</head>
</html>

"""

soup = BeautifulSoup(html_doc, "lxml")
title = soup.title
print(title)