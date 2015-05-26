import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

url1="http://web.stanford.edu/class/cs221/sample-projects/"

def stanford_ml_extract1(url):
	allIdeas=[]
	source=makeSoup(getSource(url))
	allData=source.find('table')
	allData=allData.findAll('tr')[3:9]
	for idea in allData:
		idea=idea.findAll('td')[1]
		project={}
		project['year']=2014
		project['url']=url
		project['university']="Stanford University"
		project['title']=idea.text
		project['proposal']=url1+idea.find('a').get('href') if idea.find('a') else ""
		allIdeas.append(project)
	with open('stanford_ai_2014.json','w') as outfile:
		json.dump(allIdeas,outfile,sort_keys=True, indent=4, separators=(',', ': '))

#2013-2014	
def extractProjectNLP(url):
	source=source=makeSoup(getSource(url))
	dlDiv=source.find('dl')
	allTdata=dlDiv.findAll('dt')
	allDdata=dlDiv.findAll('dd')
	projects=[]
	for data,dataD in zip(allTdata,allDdata):
		project={}
		project['title']=data.text
		project['authors']=dataD.text.replace('[Report]','')
		project['report_url']=dataD.find('a').get('href')
		project['year']=2013
		project['url']=url
		projects.append(project)
		print project
	with open('stanford_nlp_2013.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))

def extractProjectSNA(urlDetails):
	projects=[]
	for urlDetail in urlDetails:
		url=urlDetail[0]
		base_url=urlDetail[1]
		year=urlDetail[2]
		tags=["Social and Information Network Analysis","Artificial Intelligence"]
		source=makeSoup(getSource(url))
		k=source.find('ul',attrs={'id':"links-under-menu"}).extract()
		allLi=source.findAll('li')
		for li in allLi:
			project={}
			project['title']=li.text
			project['proposal']=""
			project['home_url']=url
			project['year']=year
			project['tag']=tags
			project['university']="Stanford University"
			project['authors']=[]
			if li.a:
				project['proposal']=base_url+li.a.get('href').strip("./")
			if year<=2011:
				project['title']=li.text.split(":")[0]
				try:
					project['authors']=li.text.split(":")[1]
				except:
					pass
			projects.append(project)
	with open('stanford_social_and_network_information_analysis_all.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
		

def extractProjectNLPAll(nlpUrlDetails):
	projects=[]
	for detail in nlpUrlDetails:
		url=detail[0]
		year=detail[1]
		tags=["Artificial Intelligence","Natural Language Processing"]
		source=makeSoup(getSource(url))
		allDT=source.findAll('dt')
		allDD=source.findAll('dd')
		if allDT!=[] and allDD!=[]:
			for (title,author) in zip(allDT,allDD):
				project={}
				project['title']=title.text
				project['authors']=author.text
				project['references']=[]
				project['year']=year
				project['home_url']=url
				project['tag']=tags
				if title.findAll('a')!=[]:
					for link in title.findAll('a'):
						project['references'].append([url+link.get('href'),link.text])
					
				if author.findAll('a')!=[]:
					for link in author.findAll('a'):
						project['references'].append([url+link.get('href'),link.text])
				projects.append(project)
	with open('stanford_nlp_all.json','w') as outfile:
		json.dump(projects,outfile,sort_keys=True, indent=4, separators=(',', ': '))
				
				

if __name__=='__main__':
	#stanford_ml_extract1(url1)
	url2="http://web.stanford.edu/class/cs224n/2013_projects.shtml"
	#extractProjectNLP(url2)
	urlDetails=[("http://snap.stanford.edu/class/cs224w-2010/proj2009/","http://snap.stanford.edu/class/cs224w-2010/proj2009/",2009),
                ("http://snap.stanford.edu/class/cs224w-2010/proj2010/","http://snap.stanford.edu/class/cs224w-2010/proj2010/",2010),
                ("http://snap.stanford.edu/class/cs224w-2011/proj/index.html","http://snap.stanford.edu/class/cs224w-2011/proj/",2011),
                ("http://snap.stanford.edu/class/cs224w-2012/projects.html","http://snap.stanford.edu/class/cs224w-2012/",2012),
                ("http://snap.stanford.edu/class/cs224w-2013/projects.html","http://snap.stanford.edu/class/cs224w-2013/",2013),
                ("http://web.stanford.edu/class/cs224w/projects.html","http://web.stanford.edu/class/cs224w/",2014)]
	#extractProjectSNA(urlDetails)
	nlpUrlDetails=[("http://nlp.stanford.edu/courses/cs224n/2000/",2000),
	               ("http://nlp.stanford.edu/courses/cs224n/2001",2001),
	               ("http://nlp.stanford.edu/courses/cs224n/2002",2002),
	               ("http://nlp.stanford.edu/courses/cs224n/2003/fp/",2003),
	               ("http://nlp.stanford.edu/courses/cs224n/2004/",2004),
	               ("http://nlp.stanford.edu/courses/cs224n/2005/",2005),
	               ("http://nlp.stanford.edu/courses/cs224n/2006/",2006),
	               ("http://nlp.stanford.edu/courses/cs224n/2007/fp/",2007),
	               ("http://nlp.stanford.edu/courses/cs224n/2008/",2008),
	               ("http://nlp.stanford.edu/courses/cs224n/2009/",2009),
	               ("http://nlp.stanford.edu/courses/cs224n/2010/",2010),
	               ("http://nlp.stanford.edu/courses/cs224n/2011/",2011),
	               ("http://nlp.stanford.edu/courses/cs224n/2012/",2012),]
	extractProjectNLPAll(nlpUrlDetails)
	
	
	
	
	
	
	
