import time
from selenium import webdriver
from selenium.webdriver.common.by import By								
from selenium.webdriver.support.ui import WebDriverWait						
from selenium.webdriver.support import expected_conditions as EC			
from selenium.common.exceptions import TimeoutException						
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup												
from urllib.parse import urlparse											
import sys

class Fetcher:
	def __init__(self, url):												
		options = Options()
		options.add_argument('--headless')

		self.driver = webdriver.Chrome('C:\ChromeDriver\chromedriver.exe', 
								 chrome_options=options)					
		self.driver.wait = WebDriverWait(self.driver, 5)					
		self.url = url														

	def lookup(self):
		self.driver.get(self.url)
		try:												
			ip = self.driver.wait.until(EC.presence_of_element_located(
				(By.CLASS_NAME, "gsfi")
				))
		except:
			print("Failed")

		soup = BeautifulSoup(self.driver.page_source, "html.parser")		
		answer = soup.find_all(class_= "kp-rgc")							

		if not answer:
			answer = soup.find_all(class_= "FLP8od")

		if not answer:
			answer = soup.find_all(class_= "e24Kjd")

		if not answer:
			answer = soup.find_all(class_= "di3YZe")

		if not answer:
			answer = "I can't find the answer."

		self.driver.quit()
		return answer[0].get_text()
		
