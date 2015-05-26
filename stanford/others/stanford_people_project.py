import sys
sys.path.append('/media/akash/My Passport/Dropbox/crawler')
import stanford
from stanford.utility import *

author="Nuwan Ishanta Senaratna"
base_url="http://www.cs.stanford.edu/people/nuwans"

def extractProject(url):
	source=makeSoup(getSource(url))
	tdDiv=source.findAll('td')[1]
	return 


if __name__=='__main__':
	url1="http://www.cs.stanford.edu/people/nuwans/projects.htm"
	extractProject(url1)
