
import requests
from flask import request

from bs4 import BeautifulSoup

def scrape(ab):
    wiki = requests.get(request.form['link'])
    l=[]
    soup=BeautifulSoup(wiki.text,'html.parser')
    tes=soup.find('title')
    print(tes.text+'\n')
    l.append(tes.text)
    ww2_contents=soup.find_all("div",class_='toc')
    for i in ww2_contents:
        print(i.text+'\n')
        l.append(i.text)
    print('Overview\n')
    overview=soup.find_all('table',class_='infobox vevent')
    for z in overview:
        print(z.text+'\n')
        l.append(z.text)
    return l