from utility import *



def extractProject(url):
	base_url=url
	source=makeSoup(getSource(url))
	data=source.find('tbody')
	trData=data.findAll('tr')
	projects=[]
	
	for tr in trData:
		project={}
		add_url="http://web.stanford.edu/class/cs231m/"
		tr=tr.findAll('td')
		title=tr[0]
		proposal=tr[1].find('a').get('href')
		author=tr[2]
		project['title']=title.text
		project['author']=author.text
		project['proposal']=add_url+proposal
		project['year']=2014
		project['university']="Stanford University"
		project['url']=url
		project['tag']="Mobile Vision"
		projects.append(project)
	with open('stanford_vision_2014.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
	
	
	

if __name__=='__main__':
	url1="http://web.stanford.edu/class/cs231m/projects.html"
	extractProject(url1)



