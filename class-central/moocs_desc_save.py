__author__ = 'akash'

# -*- coding: utf-8 -*-

import os
import json
import markdown
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.local'
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')


from configurations import importer
importer.install()
import django
django.setup()

from projectsearch.models import *

FilePath='/home/akash/Desktop/courses_4Feb_1.json'

jsonFile=open(FilePath)
jsonStr=jsonFile.read()
#jsonString=jsonStr.decode('unicode_escape').encode('ascii','ignore')
#print (jsonStr.decode('unicode_escape').encode('ascii','ignore'))
#print jsonString
jsonData=json.loads(jsonStr)

#print type(jsonData)

for mooc in jsonData:
    courseName=mooc['name'].encode('ascii',errors='ignore')
    start_date=mooc['date']
    descriptions=mooc['desc'].encode('ascii','ignore')
    short_description=mooc['desc_html'].encode('ascii','ignore')
    ratings=mooc['rating']
    reviews=mooc['reviews']
    try:
        mooc_list=Mooc.objects.filter(courseName=courseName)

        print courseName
        for mooc_object in mooc_list:
            mooc_object.start_date=start_date
            mooc_object.descriptions=descriptions
            mooc_object.short_description=short_description
            mooc_object.ratings=ratings
            mooc_object.reviews=reviews
            mooc_object.save()
    except Mooc.DoesNotExist as e:
        continue





