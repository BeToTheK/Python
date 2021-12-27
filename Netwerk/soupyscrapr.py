from bs4 import BeautifulSoup
import requests

with open('indextest.html') as html_file:
		soup = BeautifulSoup(html_file, 'lxml')

matchtxt = soup.title.text
match = soup.title
# print(match)
# print(matchtxt)

match1 = soup.find('p')
print(match1)