import urllib
from bs4 import BeautifulSoup
import re

url = ('http://python-data.dr-chuck.net/comments_210831.html')
html= urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")



tags = soup('span')
for tag in tags:
    wo = re.findall(('[0-9'),  str(tag))
    
    
    
