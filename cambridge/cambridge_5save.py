from mercurial.cmdutil import jsonchangeset
from mercurial.formatter import jsonformatter

__author__ = 'akash'

import os
import json
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.local'
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')


from configurations import importer
importer.install()
import django
django.setup()


from projectsearch.models import UniversityProject
from projectsearch.models import *

FilePath='/home/akash/Desktop/cambridge_5.json'

jsonFile=open(FilePath)
jsonStr=jsonFile.read()
#print type(jsonStr)
jsonData=json.loads(jsonStr)

#print type(jsonData)

for project in jsonData:
    authors=project['authors']
    description=project['description']
    home_url=project['home_url']
    img_url=project['img_url']
    levels=project['levels']
    project_url=project['project_url']
    references=project['references']
    tags=project['tags']
    title=project['title']
    type=project['type']
    year=project['year']

    university=University.objects.get(rank=4)
    university_project,flag=UniversityProject.objects.get_or_create(title=title,level='INT',home_url=home_url,
                                                                    url=project_url,image_url=img_url,
                                                                    year=int(year),score=1,university=university,
                                                                    type_of_project='MJP',long_description=description)
    print university_project

    authors=authors.strip(' \t\n\r')
    authors=authors.replace('\n',',').replace(' and ',',')
    authors=authors.split(',')

    author_list=[]
    for author in authors:
        author_list.append(Author.objects.get_or_create(name=author,types='STD')[0])

    for author in author_list:
			university_project.author.add(author)
    print author

    reference_list=[]
    for reference in references:
        if reference!='project webpage':
            reference_list.append(Reference.objects.get_or_create(name=title,link=reference)[0])

    for reference in reference_list:
        university_project.references.add(reference)
    print reference
    tag=tags[0]
    tag,flag=Tag.objects.get_or_create(name=tag)
    university_project.tags.add(tag)
    print tag



