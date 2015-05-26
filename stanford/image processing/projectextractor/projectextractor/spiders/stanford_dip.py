# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from projectextractor.items import UniversityProjectItem
from projectextractor.items import SimpleProject
from bs4 import BeautifulSoup


class StanfordImageProcessingSpider(CrawlSpider):
    name = "stanford_dip"
    allowed_domains = ["web.stanford.edu","www.stanford.edu"]
    start_urls = ('http://web.stanford.edu/class/ee368',)
    rules =(
      #Rule(LinkExtractor(allow=('Project_Spring_1314/index.html', )),callback='parse_first'),
      Rule(LinkExtractor(allow=('Project_((Spring|Winter|Autumn)_1314|(13|12))/index.html', )),callback='parse_first'),
      Rule(LinkExtractor(allow=('Project_11/index.html', )),callback='parse_second'),
      Rule(LinkExtractor(allow=('Project_10/index.html', )),callback='parse_third'),
      #Rule(LinkExtractor(allow=('Project_13/index.html', )),callback='parse_third'),
            )
        
    def parse_first(self,response):
        item=SimpleProject()
        item['url']=response.url
        year='20'+str(response.url)[:-11][-2:]
        item['year']=year
        item['university']='Stanford University'
        soup = BeautifulSoup(response.body_as_unicode())
        secondTable=soup.findAll('table')[1]
        tableRows=secondTable.findAll('tr')
        tableRows=tableRows[1:]
        for tableDiv in tableRows:
            tdTags=tableDiv.findAll('td')
            item['team']=tdTags[1].text
            item['title']=tdTags[2].text
            item['mentor']=tdTags[3].text
            proposalDiv=tdTags[4].find('a')
            item['proposal']=(proposalDiv.get('href') if proposalDiv else '')
            reportDiv=tdTags[5].find('a')
            item['report']=(reportDiv.get('href') if reportDiv else '')
            posterDiv=tdTags[6].find('a')
            item['presentation']=(posterDiv.get('href') if posterDiv else '')
            videoDiv=tdTags[7].findAll('a')
            item['video']=([link.get('href') for link in videoDiv] if videoDiv else '')
            codeDiv=tdTags[8].find('a')
            item['code']=(codeDiv.get('href') if codeDiv else '')
            yield item
        
    def parse_second(self,response):
        item=SimpleProject()
        item['url']=response.url
        year='20'+str(response.url)[:-11][-2:]
        item['year']=year
        item['university']='Stanford University'
        item['video']=""
        item['presentation']=""
        soup = BeautifulSoup(response.body_as_unicode())
        secondTable=soup.findAll('table')[1]
        tableRows=secondTable.findAll('tr')
        tableRows=tableRows[1:]
        for tableDiv in tableRows:
            tdTags=tableDiv.findAll('td')
            item['team']=tdTags[1].text
            item['title']=tdTags[2].text
            item['mentor']=tdTags[5].text
            proposalDiv=tdTags[6].find('a')
            item['proposal']=(proposalDiv.get('href') if proposalDiv else '')
            reportDiv=tdTags[7].find('a')
            item['report']=(reportDiv.get('href') if reportDiv else '')
            posterDiv=tdTags[8].find('a')
            item['poster']=(posterDiv.get('href') if posterDiv else '')
            codeDiv=tdTags[9].find('a')
            item['code']=(codeDiv.get('href') if codeDiv else '')
            yield item	
        
    def parse_third(self,response):
        item=SimpleProject()
        item['url']=response.url
        year='20'+str(response.url)[:-11][-2:]
        item['year']=year
        item['university']='Stanford University'
        item['mentor']=""
        item['video']=""
        item['presentation']=""
        soup = BeautifulSoup(response.body_as_unicode())
        secondTable=soup.findAll('table')[1]
        tableRows=secondTable.findAll('tr')
        tableRows=tableRows[1:]
        for tableDiv in tableRows:
            tdTags=tableDiv.findAll('td')
            item['team']=tdTags[1].text
            item['title']=tdTags[2].text
            proposalDiv=tdTags[4].find('a')
            item['proposal']=(proposalDiv.get('href') if proposalDiv else '')
            reportDiv=tdTags[5].find('a')
            item['report']=(reportDiv.get('href') if reportDiv else '')
            posterDiv=tdTags[6].find('a')
            item['poster']=(posterDiv.get('href') if posterDiv else '')
            codeDiv=tdTags[7].find('a')
            item['code']=(codeDiv.get('href') if codeDiv else '')
            yield item
    
    
   
        
        
			
			
			
			
			
		
    
    
	
