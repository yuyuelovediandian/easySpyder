# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:56:30 2016

@author: Administrator
"""

import urllib2

class htmldownloader():
    
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
#==============================================================================
#       print response.read()
#==============================================================================
        return response.read()
    