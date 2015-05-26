import BeautifulSoup
from BeautifulSoup import BeautifulSoup as bs4
import urllib



from projectsearch.models import University



def get_source(url):
	source=urllib.urlopen(url).read()
	return source
	

#url="file:///home/akash/Desktop/Raushan%20Data/Dropbox/ProjectMooc/ProjectMooc.com/Project%20Data/top_100_university.html"
url="/app/projectmooc/projectdata/top_100_university.html"


def get_college_details():
	source=get_source(url)
	soup=bs4(source)
	x=soup.findAll('tr')
	i=1
	details=[]
	for item in x:
		country=item.find('td',{'class':'country'}).img['alt']
		rank=i
		university=item.a.text
		#print (country,rank,university)
		i=i+1
		details.append((country,rank,university))
	return details
		
#get_college_details()
	
def insert_college_details():
	details=get_college_details()
	#print details
	for item in details:
		u=University(name=item[0],rank=item[1],country=item[2])
		u.save()


#insert_college_details()



