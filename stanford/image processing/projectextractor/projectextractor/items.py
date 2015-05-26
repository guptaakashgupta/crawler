# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# http://stackoverflow.com/questions/19068308/access-django-models-with-scrapy-defining-path-to-django-project

import scrapy
from scrapy.contrib.djangoitem import DjangoItem

from projectsearch.models import *


class ProjectmoocItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UniversityProjectItem(DjangoItem):
	django_model = UniversityProject

#mainly for stanford 
class SimpleProject(scrapy.Item):
	university=scrapy.Field()
	tags=scrapy.Field()
	url=scrapy.Field()
	title=scrapy.Field()
	report=scrapy.Field()
	team=scrapy.Field()
	mentor=scrapy.Field()
	proposal=scrapy.Field()
	report=scrapy.Field()
	poster=scrapy.Field()
	code=scrapy.Field()
	video=scrapy.Field()
	year=scrapy.Field()
	presentation=scrapy.Field()
	research_paper=scrapy.Field()
	
	
	
	
	


	
	
	
	
	
	
	
