# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:55:49 2016

@author: Administrator
"""

import UrlManage
import html_download
import html_Parser
import html_output

class SpyderMan():
    
    def __init__(self):
        self.urls = UrlManage.urlmanage()
        self.downloader = html_download.htmldownloader()
        self.parser = html_Parser.htmlparser()
        self.outputer = html_output.htmloutput()
        
    #调度管理   
    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_cont = self.downloader.download(new_url)
                print "crawl %d : %s"%(count,new_url)
                new_urls,value_data = self.parser.parse(new_url,html_cont)
                
                self.urls.add_new_urls(new_urls)
                self.outputer.collection(value_data)
                
                if count == 1000:
                    break
                
                count +=1
            except:
                print 'crawl failed'
        self.outputer.output_html()
            
    


if __name__ == "__main__":
    root_url = 'http://baike.baidu.com/view/21087.htm'
    spiderman = SpyderMan()
    spiderman.craw(root_url)
    