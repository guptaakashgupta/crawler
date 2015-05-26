# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from projectextractor.items import UniversityProjectItem
from projectextractor.items import SimpleProject
from bs4 import BeautifulSoup


class StanfordMlSpider(CrawlSpider):
    name = "stanford_ml"
    allowed_domains = ["web.stanford.edu","cs229.stanford.edu"]
    start_urls = (
        'http://cs229.stanford.edu/',
    )
    rules =(
      Rule(LinkExtractor(allow=('projects20(13|12|11|10|09|08|07|06|05).html' )),callback='parse_all'),
      )

    def parse_all(self, response):
		item=SimpleProject()
		item['url']=response.url
		#print response.url
		year=str(response.url)[:-5][-4:]
		item['year']=year
		item['university']='Stanford University'
		item['research_paper']=""
		soup = BeautifulSoup(response.body_as_unicode())
		if year=="2005" or year=="2006":
			try:
				firstProject=soup.find('b')
				item['title']=firstProject.next
				item['team']=firstProject.next.next.strip(" .")
				item['research_paper']="http://cs229.stanford.edu/"+firstProject.next.next.next.get('href')
				yield item
			except:
				pass
			
		
		projectDiv=soup.findAll('p')[2:]
		for contentPara in projectDiv:
			if contentPara.b:
				try:
					item['title']=contentPara.b.text
				except:
					item['title']=""
				try:
					item['team']=contentPara.b.next.next.strip(" .")
				except:
					item['team']=""
				if contentPara.a:
					try:
						item['research_paper']="http://cs229.stanford.edu/"+contentPara.a.get('href')
					except:
						item['research_paper']=""
			yield item
			
				
