import urllib
import json

service_url='http://python-data.dr-chuck.net/comments_210832.json'
url = urllib.urlopen(service_url).read()


info = json.loads(url)
info = info['comments']
sum=0
for item in info:
    number = item['count']
    number = int(number)
    sum= sum+number

print sum