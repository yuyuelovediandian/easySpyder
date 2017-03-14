# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:56:28 2016

@author: Administrator
"""

class urlmanage():
    
    def __init__(self):
        self.newurls = set()
        self.oldurls = set()
    
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.newurls and url not in self.oldurls:
            self.newurls.add(url)
            
    
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
        
        
        
    def get_new_url(self):
        new_url = self.newurls.pop()
        self.oldurls.add(new_url)
        return new_url
        
    def has_new_url(self):
        return len(self.newurls) != 0   