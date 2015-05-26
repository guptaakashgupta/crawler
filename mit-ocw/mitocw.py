import BeautifulSoup
from BeautifulSoup import BeautifulSoup as bs4
import urllib
import json

def getSource(url):
	source=urllib.urlopen(url).read()
	return source

def makeSoup(src):
	return bs4(src)

main_url="http://ocw.mit.edu"
parent_url="http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/"


def getAllCourse(url):
	soup=makeSoup(getSource(url))
	tableDiv=soup.find('table',attrs={'class':'courseList'})
	tableList=tableDiv.find('tbody')
	trList=tableList.findAll('tr')
	courses=[]
	urls=[]
	for id,tr in enumerate(trList):
		course={}
		tdList=tr.findAll('td')
		jsonUrl=main_url+tdList[1].find('a').get('href')+"/index.json"
		print id,jsonUrl
		src=getSource(jsonUrl)
		data=json.loads(src)
		courses.append(data)
		with open('mit_ocw_dummy.json','w') as outfile:
			json.dump(courses,outfile,sort_keys=True, indent=4, separators=(',', ': ')) 
	
		

getAllCourse(parent_url)
