import urllib
from bs4 import BeautifulSoup
import re

url = ('https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Tehya.html')
html= urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")
list=[]

tags = soup('a')
for tag in tags:
    list.append(tag.get('href', None))

print list[17]






