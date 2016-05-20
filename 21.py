import urllib
import xml.etree.ElementTree as ET

url = ('http://python-data.dr-chuck.net/comments_210828.xml')

data = urllib.urlopen(url).read()
tree = ET.fromstring(data)

sum= 0

counts = tree.findall('.//count')
for count in counts:
    count = count.text
    number = int(count)
    sum = sum+number    

print sum