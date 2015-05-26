# -*- coding: utf-8 -*-

# Scrapy settings for projectextractor project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'projectextractor'

SPIDER_MODULES = ['projectextractor.spiders']
NEWSPIDER_MODULE = 'projectextractor.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'projectextractor (+http://www.yourdomain.com)'

import sys
sys.path.insert(0,'/home/akash/Desktop/RaushanData/Dropbox/ProjectMooc/ProjectMooc.com/codes/projectmooc/projectmooc')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.local'
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

from configurations import importer
importer.install()
