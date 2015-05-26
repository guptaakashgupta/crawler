import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

def extractProject(url):
	source=makeSoup(getSource(url))
	allTable=source.find('table',attrs={'class':'table'})
	allTr=allTable.findAll('tr')
	projects=[]
	title_text=""
	for Tr in allTr:
		project={}
		td=Tr.findAll('td')
		if len(td)==1:
			title_text=td[0].text
			print title_text
		else:
			project['title']=td[0].h3.text
			project['project_url']=td[0].h3.a.get('href')
			project['home_url']=url
			project['year']=2014
			project['tags']="hci"
			project['university']="Stanford University"
			project['description']=title_text+" | "+td[1].text
			project['authors']=td[0].h4.text
			projects.append(project)
			project={}
			try:
				project['title']=td[2].h3.text
				project['project_url']=td[2].h3.a.get('href')
				project['home_url']=url
				project['year']=2014
				project['tags']="hci"
				project['university']="Stanford University"
				project['description']=title_text+" | "+td[3].text
				project['authors']=td[2].h4.text
				projects.append(project)
			except:
				pass
		with open('stanford_hci_project_2014.json','w') as outfile:
			json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
			

def extractResearch(url):
	year=2014
	base_url="http://hci.stanford.edu/research/"
	source=makeSoup(getSource(url))
	allArticles=source.findAll('article')
	new_projects=allArticles[0].findAll('li')
	new_projects.pop(3)
	projects=[]
	for index,item in enumerate(new_projects):
		if index>5:
			year=2013
		project={}
		try:
			project['project_url']=item.a.get('href')
			project['title']=item.a.text
			project['description']=item.findAll('span')[1].text
			project['type']="Research"
			project['year']=year
			project['tags']='hci'
			project['home_url']=url
			projects.append(project)
		except:
			pass
	with open('stanford_hci_researchproject_2014_2013.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
	
		


if __name__=='__main__':
	url1="http://hci.stanford.edu/courses/cs147/2014/au/projects.html"
	#extractProject(url1)
	url2="http://hci.stanford.edu/research/"
	extractResearch(url2)
