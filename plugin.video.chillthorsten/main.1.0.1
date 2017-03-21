
# -*- coding: utf-8 -*-

import sys
from urllib import urlencode
from urllib2 import urlopen # Weil Python2.x
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin
import xbmcaddon
import re

#############################

# To do: 
# in ../testen mit der Datei hole_video.py versuchen, Listen von chilloutzone zu holen mit den Werten:
# URL, TITEL, mit dem aktuellen Datum bis in die Vergangenheit

class Chillkodi(): 
	def __init__(self,anzahl_urls):
		''' Initiieren durch holen der wichtigen Daten mittels der ersten URL aus übergebenen Variable anchor. Muss später aus irgendeiner config-Datei geladen werden '''
		self._Anzahl_URLS = anzahl_urls	
		self._URL = self.hole_neuste_url() # Übergeben der Start-URL
		self._Page = self.page_holen(self._URL)
		self._picture = ""
		self.hole_picture()
	#	self._Datum = self.hole_Datum() # Struktur _Datum[0] - Jahr , _Datum[1] - Monat , _Datum[2] - Tag
		self.hole_titel()
		self.hole_videolink()
		''' Hier noch Konstant, kann später noch angepasst werden '''
		self.li = xbmcgui.ListItem(self.titel, iconImage=self._picture)
		self.Add_Video()	
#		
		self.Lade_Liste()

	def hole_picture(self):
		''' Bild als Vorschaubild '''
		picture = re.findall(r"http.*jpg",self._Page)	
		self._picture = picture[0]

	def hole_neuste_url(self):
		_startpage = self.page_holen('http://www.chilloutzone.net/')
		first_match = re.search(r"(h2.*)(/video.*html)(.*h2)",_startpage)
		if (first_match != None):
			first_match = first_match.group(2)
			newesturl = "http://www.chilloutzone.net"+first_match
		return newesturl		


	def Testen(self):
		self.Testadd("Hier müssen jetzt neue Videos, immer wenn man auf weiter drückt")	
		self.Lade_Next()
		self.Add_Video()
	def Lade_Liste_mit_Anchor_URL_alte_Version(self):
		''' Schleife solange, bis Lade_Next None zurück gibt '''
		next =""
		while (next != None):
			next = self.Lade_Next()
			self.Add_Video()
		
	def Lade_Liste(self):
		''' Schleife solange, bis Lade_Next None zurück gibt oder die Gesamtanzahl an Videos erreicht ist '''
		x = 0	
		next =""
		while (next != None and x < self._Anzahl_URLS):
			next = self.Lade_Next()
			self.Add_Video()
			x = x + 1

	def Lade_Next(self):	
		''' Das von der aktuellen Seite self._Page ausgehend nächste Video wird von hier aus geladen ''' 
		next = re.search(r"(http.*\.html)(.*Älter)",self._Page)
		if next != None:
			self._URL = next.group(1)	
			self._Page = self.page_holen(self._URL)
			self.hole_titel()
			self.hole_videolink()
			self.hole_titel()
			self.hole_picture()
			self.li = xbmcgui.ListItem(self.titel, iconImage=self._picture)		
		
		return next # Gibt None zurück, wenn ein Fehler auftritt, wenn es zum Beispiel das Neuste Video ist

	def Testadd(self,Testwert):
		li = xbmcgui.ListItem(Testwert, iconImage='http://eu6.cdn.internetz.me/coz/_images/thumbnails/22100/22110-bohrmaschinensaufen-5571b788e97ea-150x90.jpg')
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=self.videolink, listitem=li)

	def page_holen(self, url): # Herunterladen einer URL
		resp = urlopen(url)
		contents = resp.read()
		return contents

	def hole_titel(self):
		self.titel = re.search(r"(contentTitle)(.*)(=)(.*)(;)",self._Page)
		if self.titel is not None:
			self.titel = self.titel.group(4)
			self.titel = (self.titel[2:len(self.titel)-1])
		else:
			self.titel = "Kein Titel gefunden"	

	def hole_videolink(self):
		self.videolink = re.search(r"(MOVIE_LOC_PLAIN)(.*)(http.*mp4)",self._Page)
		if self.videolink is not None:
			self.videolink = self.videolink.group(3)
		else:
			self.videolink = "Kein Link gefunden"	

	def Add_Video(self):
		''' Hinzufügen des Videos, nachdem mit Lade_Next alle Daten geholt wurden '''	
		xbmcplugin.addDirectoryItem(handle=addon_handle, url=self.videolink, listitem=self.li)



	# Vorbereitung
addon_handle = int(sys.argv[1])
	# Dass es um Videos geht
xbmcplugin.setContent(addon_handle, 'movies')
# Das mit dem Parser funktioniert nicht
	
	# Erste Seite und Chillkodi mit ck initialisieren
#anchor_url = "http://www.chilloutzone.net/video/anti-vorfreude-auf-ostern.html"
settings = xbmcaddon.Addon()
try:
	anzahl_urls = int(settings.getSetting('anzahl_urls'))
except ValueError:
	print("Ein Fehler ist aufgetreten. In der settings.xml muss bei anzahl_urls eine ganze Zahl stehen. Bitte überprüfen")
	exit()

ck = Chillkodi(anzahl_urls)


xbmcplugin.endOfDirectory(addon_handle)





