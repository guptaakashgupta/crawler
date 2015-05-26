import BeautifulSoup
from BeautifulSoup import BeautifulSoup as bs4
import urllib
import json

def getSource(url):
	source=urllib.urlopen(url).read()
	return source

def makeSoup(src):
	return bs4(src)




