from sys import *
import requests
from bs4 import BeautifulSoup


response = requests.get(argv[1])
# html_content = response.text
soup = BeautifulSoup(response.text,'html.parser')

print(soup.title.string)
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())

# for x in argv :
#     print("values:", x)