
import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *


#downloads url and project url are same ,parent source url = url
def extractProject(url):
	base_url=url
	source=makeSoup(getSource(url))
	data=source.find('ul')
	liData=data.findAll('li')
	projects=[]
	
	for li in liData:
		project={}
		project['downloads']=li.find('a').get('href')
		project['title']=li.find('a').text
		project['author']=li.find('i').text
		project['year']=2014
		project['university']="Stanford University"
		project['url']=url
		project['project_url']=li.find('a').get('href')
		project['tag']="Music Computing"
		project['short_description']=li.find('i').next.next.next
		projects.append(project)
	with open('stanford_music_2014.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
	
	
	

if __name__=='__main__':
	url1="https://ccrma.stanford.edu/courses/256a/projects/"
	extractProject(url1)
