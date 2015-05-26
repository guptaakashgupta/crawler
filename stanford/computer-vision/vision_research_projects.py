import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

def extractProject(url):
	base_url="http://cvgl.stanford.edu/research"
	source=makeSoup(getSource(url))
	tBody=source.findAll('tbody')[0]
	allTr=tBody.findAll('tr')
	projects=[]
	for trs in allTr:
		project={}
		try:
			tds=trs.findAll('td')
			img=tds[0].img.get('src')
			project['image_url']=img
			allDetails=tds[1].p.contents
			project['tag']="Computer Vision"
			project['title']=allDetails[1].text
			project['description']=allDetails[4]
			project['base_url']=base_url
			project['home_url']=url
			project['project_url']=""
			try:
				project['project_url']=""
			except:
				pass
			allLinks=tds[1].p.findAll('a')
			if allLinks!=[]:
				project['references']=[(item.get('href'),item.text) for item in allLinks ]
			else:
				allLinks=[]
		except:
			pass
		projects.append(project)
		
	tBody=source.findAll('tbody')[1]
	allTr=tBody.findAll('tr')
	for trs in allTr:
		project={}
		try:
			tds=trs.findAll('td')
			img=tds[0].img.get('src')
			project['image_url']=img
			allDetails=tds[1].p.contents
			project['tag']="Computer Vision"
			project['title']=allDetails[1].text
			project['description']=allDetails[4]
			project['base_url']=base_url
			project['home_url']=url
			project['project_url']=""
			try:
				project['project_url']=""
			except:
				pass
			allLinks=tds[1].p.findAll('a')
			if allLinks!=[]:
				project['references']=[(item.get('href'),item.text) for item in allLinks ]
			else:
				allLinks=[]
		except:
			pass
		projects.append(project)
	with open('stanford_vision_research_projects.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
	
		


if __name__=='__main__':
	url1="http://cvgl.stanford.edu/research.html"
	extractProject(url1)
