import urllib
from bs4 import BeautifulSoup
import re

url = ('http://python-data.dr-chuck.net/comments_210831.html')
html= urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

list=[]

tags = soup('span')
for tag in tags:
    list.append(int(tag.get_text()))
sum=0   
for number in list:
    sum = sum+number
print sum

    
    
    
