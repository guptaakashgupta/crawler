from utility import *

#function to extract data mining stanford project 2014 | Ideas
url1="http://web.stanford.edu/class/cs341/projects.html"
def data_mining_extract(url):
	source=makeSoup(getSource(url))
	projectUl=source.findAll('ul')[1]
	projects=[]
	projectAll=projectUl.findAll('li')
	for li in projectAll:
		project={}
		if li.find('a') is not None:
			href=li.find('a').get('href')
		else:
			href=""
		alltext=li.text
		titleAuthor=alltext.split('by')
		author=titleAuthor[1]
		title=titleAuthor[0]
		project['author']=author
		project['title']=title
		project['proposal']=href
		project['year']=2014
		project['university']="Stanford University"
		project['url']="http://web.stanford.edu/class/cs341/projects.html"
		projects.append(project)
	with open('stanford_data_mining_2014.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
#data_mining_extract(url1)


#fuction to extract data mining project stanford ideas only
url2="http://snap.stanford.edu/class/cs345a-2010/project.html"

def data_mining_extract2(url):
	allIdeas=[]
	
	source=makeSoup(getSource(url))
	allData=source.findAll('ul')[3]
	allData=allData.findAll('li')
	for idea in allData:
		project={}
		project['year']=2010
		project['url']=url
		project['university']="Stanford University"
		project['title']=idea.text
		allIdeas.append(project)
	#print allData
	mainIdea=source.findAll('ul')[5]
	mainIdea=mainIdea.findAll('li')
	for idea in mainIdea:
		project={}
		project['year']=2010
		project['url']=url
		project['university']="Stanford University"
		project['title']=idea.text
		allIdeas.append(project)
	with open('stanford_data_mining_2010.json','w') as outfile:
		json.dump(allIdeas,outfile,sort_keys=True, indent=4, separators=(',', ': '))

    
#data_mining_extract2(url2)
	
url3="http://web.stanford.edu/class/cs341/projects.html"

def data_mining_extract3(url):
	allIdeas=[]
	source=source=makeSoup(getSource(url))
	allData=source.findAll('ul')[1]
	allData=allData.findAll('li')
	for idea in allData:
		project={}
		project['year']=2014
		project['url']=url
		project['university']="Stanford University"
		#print idea.text
		project['title']=idea.text.rsplit('by',1)[0]
		project['authors']=idea.text.rsplit('by',1)[1]
		project['proposal']=idea.find('a').get('href') if idea.find('a') else ""
		allIdeas.append(project)
	with open('stanford_data_mining_2014_diff1.json','w') as outfile:
		json.dump(allIdeas,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		

if __name__=='__main__':
	data_mining_extract3(url3)



