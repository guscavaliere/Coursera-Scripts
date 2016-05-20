import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
address ='Virginia Tech'
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
url= urllib.urlopen(url).read()


js = json.loads(url)
js = js["results"][0]["place_id"]
print js


