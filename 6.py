import urllib
from bs4 import BeautifulSoup
import re

url = ('http://python-data.dr-chuck.net/comments_210831.html')
html= urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tag = soup('span')
print tag

list=[]

for tags in tag:
    tags.rstrip()
    list.append(tags)