from bs4 import BeautifulSoup as bs
import urllib2
import json
base_url="http://ri.cmu.edu/"


current_url="http://ri.cmu.edu/research_project_view.html?category_id=11&type=alphabet&list_type=current&menu_id=261&selected_letter=All"
past_url="http://ri.cmu.edu/research_project_view.html?menu_id=261&list_type=past&type=alphabet&selected_letter=All&category_id=11"

source=bs(urllib2.urlopen(past_url).read())
allTr=source.findAll('tr')
projects=[]
for trs in allTr:
    allTds=trs.findAll('td')
   
    if len(allTds)==3:
        try:
            project={}
            project['tags']="Robotics"
            project['University']="CMU"
            project['img_src']=base_url+allTds[0].img.get('src').strip('/')
            project['project_url']=base_url+allTds[2].find('a').get('href')
            project['title']=allTds[2].find('a').text
            k=allTds[2].find('a').extract()
            project['description']=allTds[2].text
            #project['year']=2014
            projects.append(project)
            print project
        except:
            pass
with open('robotics_past_research.json','w') as outfile:
	json.dump(courses,outfile,sort_keys=True, indent=4, separators=(',', ': ')) 
           
     
       
        
