from sys import *
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome()
driver.get(argv[1])
time.sleep(5)
html_content = driver.page_source

driver.quit()

soup = BeautifulSoup(html_content,'html.parser')
#print title
print("\n Title:")
print(soup.title.string)

#print all links
print("\nLinks:")

for link in soup.find_all('a'):
    href = link.get('href')

    if href .startswith("http"):
        print(href)

#print full text
print("\nFull page text:")
print(soup.get_text())

