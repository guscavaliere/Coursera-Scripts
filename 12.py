import urllib
from bs4 import BeautifulSoup
import re

url = raw_input ('Enter - ')
html= urllib.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

list = []

tags = soup('span')
for tag in tags:
    list.append(tag)
    
final=[]
final1=[]
    
for number in list:
    numbers = number.strip()
    final.append(numbers)
    for usual in final:
        if int(usual)== True:
            final1.append(usual)
        else:
            continue
            
print final1
    
        

    


    
    
