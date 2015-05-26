from utility import *



def extractProject(url):
	base_url="http://suif.stanford.edu/~courses/cs294s/"
	source=makeSoup(getSource(url))
	titles=source.findAll('p',attrs={'class':'title'})
	authors=source.findAll('p',attrs={'class':'students'})
	projects=[]
	for (item,title)in zip(authors,titles):
		project={}
		links=item.findAll('a')
		try:
			proposal=base_url+links[0].get('href')
			video=links[1].get('href')
		except:
			proposal=""
			video=""
		names=item.next
		project['title']=title.text
		project['author']=names
		project['video']=video
		project['proposal']=proposal
		project['year']=2012
		project['university']="Stanford University"
		project['url']="http://suif.stanford.edu/~courses/cs294s/projects.html"
		project['tag']="Mobile and Social Computing Systems"
		projects.append(project)
	with open('stanford_game_2012.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		
	
	
	

if __name__=='__main__':
	url1="http://suif.stanford.edu/~courses/cs294s/projects.html"
	extractProject(url1)



