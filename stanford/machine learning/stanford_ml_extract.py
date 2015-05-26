import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

def extractProject(url):
	source=makeSoup(getSource(url))
	pDivs=source.findAll('p')[4:]
	projects=[]
	for pDiv in pDivs:
		project={}
		details=pDiv.contents
		project['title']=details[1].text
		project['url']=url
		project['author_name']=details[2].split('(')[0].strip(". ")
		project['author_email']=details[2].split('(')[1].strip(".) ")
		project['description']=details[4]
		project['year']=2012
		projects.append(project)
	with open('stanford_ml_project_2012.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
		
		


if __name__=='__main__':
	url1="http://cs229.stanford.edu/projectIdeas_2012.html"
	extractProject(url1)
