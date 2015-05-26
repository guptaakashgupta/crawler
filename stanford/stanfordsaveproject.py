
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.local'
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')


from configurations import importer
importer.install()
import django
django.setup()

import json
from projectsearch.models import UniversityProject
from projectsearch.models import *

stanford_dip_ee368="stanford_dip_ee368.json"
stanford_ml_cs229="stanford_ml_data_cs229.json"


def read_json(path):
	json_data=open(path)
	data=json.load(json_data)
	return data

#save stanford projects of dip to database
def stanford_dip():
	data=read_json(stanford_dip_ee368)
	#print item['university'],item['code'],item['title'],item['url'],
	#item['team'],item['video'],item['year'],item['presentation'],item
	#['mentor'],item['proposal'],item['report'],item['poster']
	university=University.objects.get(rank=2)
	dip_tag=Tag.objects.get_or_create(name="image-processing")
	
	for project in data:
		title=project['title']
		title=' '.join(title.split())
		url=project['url']
		tag_head=dip_tag[0]
		video_url=project['video']
		#authors=project['team'].strip(' \t\n\r')
		#authors=authors.split('\n')
		authors=project['team'].strip(' \t\n\r')
		authors=authors.replace('\n',',').replace(' and ',',')
		authors=authors.split(',')
		authors_list=[]
		for author in authors:
			if author.strip()!="":
				author=author.strip(' \t\n\r')
				author=author.strip('.')
				authors_list.append(Author.objects.get_or_create(name=author,types='STD')[0])	
		year=project['year']
		code=project['code']
		mentors=project['mentor'].strip(' \t\n\r')
		mentors=mentors.replace('\n',',').replace(' and ',',')
		mentors=mentors.split(',')
		for mentor in mentors:
			if mentor!="":
				authors_list.append(Author.objects.get_or_create(name=mentor.strip('.'),types='MEN')[0])
		score=1
		downloads=[]
		if project['video']!="":
			for item in project['video']:
				download_video=Download.objects.get_or_create(name=title+" video",download_type='VID',url=item)[0]
				downloads.append(download_video)
		if project['code']!="":
			download_code=Download.objects.get_or_create(name=title+" code",download_type='COMP',url=project['code'])[0]
			downloads.append(download_code)
		if project['presentation']!="":
			download_presentation=Download.objects.get_or_create(name=title+" presentation/poster ppt",download_type='DOC',url=project['presentation'])[0]
			downloads.append(download_presentation)
		if project['proposal']!="":
			download_proposal=Download.objects.get_or_create(name=title+" proposal pdf",download_type='DOC',url=project['proposal'])[0]
			downloads.append(download_proposal)
		if project['report']!="":
			download_report=Download.objects.get_or_create(name=title+" report pdf",download_type='DOC',url=project['report'])[0]
			downloads.append(download_report)
		if project['poster']!="":
			download_poster=Download.objects.get_or_create(name=title+" poster pdf",download_type='DOC',url=project['poster'])[0]
			downloads.append(download_poster)	
		university_project=UniversityProject.objects.get_or_create(title=title,url=url,year=year,score=score,university=university)[0]
		for download in downloads:
			university_project.downloads.add(download)
		for author in authors_list:
			university_project.author.add(author)
		university_project.tags.add(tag_head)
		print university_project
		
def stanford_ml():
	data=read_json(stanford_ml_cs229)
	university=University.objects.get(rank=2)
	ml_tag=TagHead.objects.get_or_create(name="machine-learning")[0]
	for index,project in enumerate(data):
		authors_list=[]
		title=' '.join(project['title'].split())
		proposal=project['research_paper']
		url=project['url']
		year=project['year']
		authors=project['team'].strip(' \t\n\r')
		authors=authors.replace('\n',',').replace(' and ',',')
		authors=authors.split(',')
		download_proposal=Download.objects.get_or_create(name=title[0:30]+" proposal pdf",download_type='DOC',url=project['research_paper'])[0]
		for author in authors:
			if author.strip()!="":
				author=author.strip(' \t\n\r')
				author=author.strip('.')
				authors_list.append(Author.objects.get_or_create(name=author,types='STD')[0])
		university_project,flag=UniversityProject.objects.get_or_create(title=title,url=url,year=year,score=1,university=university)
		for author in authors_list:
			university_project.author.add(author)
		university_project.tags.add(ml_tag)
		print university_project
		
	
		
	
	
stanford_ml()
stanford_dip()
# ALL CALL TO EXECUTERS GO HERE	
#stanford_dip()
