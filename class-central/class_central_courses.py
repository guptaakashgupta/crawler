#crawler for class central computer science courses

import BeautifulSoup
from BeautifulSoup import BeautifulSoup as bs4
import urllib
import json
import html2text

def get_source(url):
	source=urllib.urlopen(url).read()
	return source


url="courses.html"

def all_courses():
	courses=[]
	src=get_source(url)
	soup=bs4(src)
	allEventTr=soup.findAll('tr',attrs={'itemtype':"http://schema.org/Event"})
	
	for id,event in enumerate(allEventTr):
		course={}
		
		name=event.find('span',attrs={'itemprop':"name"}).text
		provider=event.find('div',attrs={'class':"course-provider"}).text
		start_date=event.find('div',attrs={'class':"course-startdate"}).text
		rating=event.find('div',attrs={'class':"course-rating-value"}).text
		university_list=event.findAll('a',attrs={'class':"uni-name"})
		reviews=event.find('a',attrs={'class':'number-of-ratings-bubble'}).text
		universities=[]
		for item in university_list:
			if item:
				universities.append(item.text)
			
		
		via_url=event.find('a',attrs={'class':"course-name"}).get('href')
		#course page
		soup=bs4(get_source(via_url).decode('utf-8'))
		course_url=soup.find('a',attrs={'class':"register-button"}).get('href')
		k=soup.find('div',attrs={'class':"course-desc"})
		course_desc=k.text
		course_desc_html=html2text.html2text(str(k).decode('utf-8'))
		video_url=""
		video_temp=soup.find('iframe',attrs={'class':"ytb-video-frame"})
		if video_temp:
			video_url=video_temp.get('src')
		course['name']=name
		course['provider']=provider
		course['university']=universities
		course['date']=start_date
		course['rating']=rating
		course['url']=course_url
		course['desc']=course_desc
		course['desc_html']=course_desc_html
		course['reviews']=reviews
		course['video_url']=video_url
		courses.append(course)
		print id,name
		with open('courses_4Feb_1.json','w') as outfile:
			json.dump(courses,outfile,sort_keys=True, indent=4, separators=(',', ': ')) 

all_courses()
