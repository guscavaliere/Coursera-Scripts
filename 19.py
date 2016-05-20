import urllib
from bs4 import BeautifulSoup
import re

url = ('http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html')
html= urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")
list=[]

tags=soup('a')
count=0
for tag in tags:
    list.append(tag.get('href', None))
    while count < 4:
        url = list [2]
        html= urllib.urlopen(url).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup('a')
        for tag in tags:
            tags[2] = list[2]
    





