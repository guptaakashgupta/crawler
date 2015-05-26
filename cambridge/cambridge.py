import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

#Cambridge

def extractProject(url):
	source=makeSoup(getSource(url))
	base_url="https://www.cl.cam.ac.uk/research/dtg/www/"
	divs=source.findAll('div',attrs={'class':'proj-entry'})
	projects=[]
	for item in divs:
		project={}
		project['title']=item.find('a').text
		project['home_url']=url
		project['project_url']=item.find('a').get('href')
		project['description']=item.find('div',attrs={'class':'summary'}).text
		project['authors']=[span.text.strip('*') for span in item.find('div',attrs={'class':'members'}).findAll('span')]
		project["img_url"]=base_url+item.find('img',attrs={'class':'projimage'}).get('src').strip('./')
		project["downloads"]=""
		project['tags']=["Digital Technology"]
		project['university']="cambridge"
		project['year']="2014"
		project["type"]="Research"
		project["levels"]="Advance"
		k=[spans.extract() for spans in item.findAll('span')]
		project["references"]=[link.get('href') for link in item.findAll('a')]
		print project
		projects.append(project)
	with open('cambridge_3.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
	
def extractProjectAndroid(url):
	source=makeSoup(getSource(url))
	base_url=url
	divs=source.findAll('h2')
	projects=[]
	for item in divs:
		project={}
		if item.findNext('h3'):
			short_title=item.findNext('h3').text
		else:
			short_title=""
		project['title']=item.text + ": " + short_title
		project["img_url"]=base_url+item.find('img').get('src')
		project['home_url']=url
		if item.find('a'):
			project['project_url']=item.find('a').get('href')
		else:
			project['project_url']=""
		p1=item.findNext('p')
		p2=item.findNext('i').findPrevious('p')
		project['description']=item.findNext('p').text
		project['authors']=item.findNext('i').text.strip("Summer placement project, written by")
		project["downloads"]=""
		m=[[link.get('href'),link.text] for link in p1.findAll('a')]
		m.extend([[link.get('href'),link.text] for link in p1.findAll('a')])
		project["references"]=m
		project['tags']=["Digital Technology","Android","Mobile Technology"]
		project['university']="cambridge"
		project['year']="2014"
		project["type"]="Final Year"
		project["levels"]="Intermediate"
		
		print project
		projects.append(project)
	with open('cambridge_5.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))	


if __name__=='__main__':
	url1="https://www.cl.cam.ac.uk/research/dtg/www/research/"
	#extractProject(url1)
	url2="https://www.cl.cam.ac.uk/research/dtg/android/"
	extractProjectAndroid(url2)
	
