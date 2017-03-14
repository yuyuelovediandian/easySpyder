# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:56:30 2016

@author: Administrator
"""

from bs4 import BeautifulSoup 
import re
import urlparse

class htmlparser():
    
    def _get_new_links(self,url_page,soup):
        new_links = set()
        # <a target="_blank" href="/view/20965.htm">自由软件</a>
        links = soup.find_all('a',href = re.compile(r"/view/\d+\.htm"))
#==============================================================================
#         print links
#==============================================================================
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url_page,new_url)
            new_links.add(new_full_url)
#==============================================================================
#         print new_links
#==============================================================================
        return new_links
        
        
    def _get_new_data(self,url_page,soup):
        res_data = {}
        res_data['url'] = url_page
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_ = "lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        print res_data['title']
       # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = "lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data
    
    
    def parse(self,url_page,url_cont):
        if url_page is None or url_cont is None:
            return
        soup = BeautifulSoup(url_cont,'html.parser',from_encoding = 'utf-8')
        #print soup.find('a')
        new_urls = self._get_new_links(url_page,soup)
        new_data = self._get_new_data(url_page,soup)
        #print new_data
        return new_urls,new_data
        

