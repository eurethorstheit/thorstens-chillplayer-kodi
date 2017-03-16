
# -*- coding: utf-8 -*-

import sys, re
from urllib2 import urlopen # Weil Python2.x

def find_picture(_page):
	picture = re.findall(r"http.*jpg",_page)	
	return picture
def page_holen(url): # Herunterladen einer URL
	resp = urlopen(url)
	contents = resp.read()
	return contents

url = "http://www.chilloutzone.net/video/iphone-6-mit-kleiner-ueberraschung.html"

_page = page_holen(url)
_picture = find_picture(_page)
print(_picture[0])

