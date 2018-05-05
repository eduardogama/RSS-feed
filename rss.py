import feedparser
import os
import unidecode

 
 
########################################################################
class RSS(object):
    """
    RSS object
    """
 
    #----------------------------------------------------------------------
    def __init__(self, title, link, website, summary, all_data):
        """Constructor"""
        self.title = title
        self.link = link
        self.all_data = all_data
        self.website = website
        self.summary = summary

