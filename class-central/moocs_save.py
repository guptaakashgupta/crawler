# -*- coding: utf-8 -*-
from _ast import unaryop

__author__ = 'akash'

import os
import json
import csv
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.local'
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')


from configurations import importer
importer.install()
import django
django.setup()

from projectsearch.models import *

FilePath='/media/akash/My Passport/Dropbox/crawler/class-central/courses.csv'

file=open(FilePath,'rt')

reader=csv.reader(file)
flag=1
for entry in reader:
    if(flag==1):
        flag=flag+1
        continue
    #print entry
    courseId=entry[0]
    courseName=str(entry[1])
    parentSubject=str(entry[4])
    childSubject=str(entry[5])
    url=str(entry[6])
    start_date=entry[7]
    length=entry[8]
    video_image=str(entry[9])

    universityName=str(entry[3])
    providerName=str(entry[2])

    if length=='':
        length=0
    print courseId,courseName,parentSubject,childSubject,url,start_date,length,video_image,universityName,providerName

    university,flag=University.objects.get_or_create(name=universityName)
    #print university

    provider,flag=MoocProvider.objects.get_or_create(name=providerName)
    #print provider

    moocObject,flag=Mooc.objects.get_or_create(courseId=courseId,courseName=courseName,parentSubject=parentSubject,
                                                childSubject=childSubject,url=url,
                                                length=length,video_image=video_image,
                                                provider=provider)
    print moocObject
    moocObject.universities.add(university)




