import pprint
import feedparser
import xml.etree.ElementTree as ET
import json

import rss


class Website():
	def __init__(self, title, url, keys=[]):
		self.title = title
		self.url = url
		self.keys = keys
		
# Function grabs the rss feed headlines(titles) and returns them as a list
def getHeadlines(rss_url):
	headlines = []
	
	feed = feedparser.parse(rss_url)

	for newsitem in feed['items'] :
		headlines.append(newsitem['title'])    

	return headlines
	
#def getRSS():
	

if __name__ == '__main__' :

	with open('config.json') as json_data_files:
		newsurls = json.load(json_data_files)
	
	#A list to hold all headlines
	allheadlines = []
	
	listItem = []
	for item in newsurls['website'].items():
		i = item[1]
		if not i['shutdown']:
			if i['feed']:
				listItem.append(Website(item[0],i['url']))
			else:
				listItem.append(Website(item[0],i['url'],i['attr']))
					
	# Iterate over the feed urls
	for key,url in newsurls['website'].items():
		# Call getHeadlines() and combine the returned headlines with allheadlines
		allheadlines.extend(getHeadlines(url))
	 
	# Iterate over the allheadlines list and print each headline
	for hl in allheadlines:
		print(hl)

