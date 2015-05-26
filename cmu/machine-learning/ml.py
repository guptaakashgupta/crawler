import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

def extractProject(url):
	projects=[]
	year=2014
	base_url="http://www.ml.cmu.edu/research/"
	source=makeSoup(getSource(url))
	table=source.find('table',attrs={"border":"0"})
	allTr=table.findAll('tr')
	
	for tr in allTr:
		td=tr.findAll('td')
		project={}
		project['img_src']=base_url+td[0].find('img').get('src')
		project['year']='year'
		project['project_url']=
	
	

if __name__=='__main__':
	url1="http://www.ml.cmu.edu/research/index.html"
	extractProject(url1)
	url2=""
	#extractMLProjectReports()
	url3=""
	#extractDataAnalysisReports()
