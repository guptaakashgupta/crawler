
import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

base_url="https://cs.stanford.edu"
def extractProject(url):
	source=makeSoup(getSource(url))
	tbodyDiv=source.find('tbody')
	trDiv=tbodyDiv.findAll('tr')
	projects=[]
	for tr in trDiv:
		project={}
		tds=tr.findAll('td')
		project['title']=tds[0].text
		project['project_url']=base_url+tds[0].find('a').get('href')
		project['type']="research"
		project['home_url']=url
		project['image_url']=tds[1].find('img').get('src')
		project['description']=tds[2].text
		projects.append(project)
	with open('stanford_research_projects.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		

#forum based researches
def extractForumProject(url):
	base_url1="https://forum.stanford.edu"
	source=makeSoup(getSource(url))
	divs=source.findAll("div",attrs={'style':"padding-top: 10px;"})
	projects=[]
	for div in divs:
		project={}
		project['title']=div.find('p').text
		project['university']="Stanford University"
		project['type']="Research Project"
		project['home_url']=url
		project['authors']=[]
		project['description']=div.find('div',attrs={'style':"font-weight: normal;"}).text
		project['image_url']=base_url1+div.find('img').get('src').strip('.')
		project['project_url']=div.find('div',attrs={'class':"projbts"}).find('a').get('href')
		#print project['image_url']
		author_details=div.find('table').tr.findAll('td')[0].findAll('a')
		for item in author_details:
			project['authors'].append(item.text)
		
		project_tags=div.find('table').tr.findAll('td')[1].findAll('a')
		project['tags']=[]
		for item in project_tags:
			project['tags'].append(item.text)
		projects.append(project)
		
	with open('stanford_forum_research_projects.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
		
			
		
	
	

if __name__=='__main__':
	url1="https://cs.stanford.edu/research/projects"
	#extractProject(url1)
	url2="https://forum.stanford.edu/research/projects.php"
	extractForumProject(url2)

