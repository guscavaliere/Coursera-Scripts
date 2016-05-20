import urllib
from bs4 import BeautifulSoup
import re



def fhand(x):
    count=0
    while count<7:
        html= urllib.urlopen(x).read()
        soup = BeautifulSoup(html, "html.parser")
        list=[]
        tags = soup('a')
        for tag in tags:
            list.append(tag.get('href', None))
        print list[17]
        x=str(list[17])
    count=count+1
        

url = ('https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Manus.html')
fhand(url)