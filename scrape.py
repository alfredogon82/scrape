from bs4 import BeautifulSoup
import requests
url = 'http://www.blabbermouth.net'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'lxml')
meta = soup.find_all("h1", {"class": "newsh1"})

#print(meta[0].text.strip())
for x in meta:
  print(x.text.strip())



