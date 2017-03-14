# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:56:31 2016

@author: Administrator
"""

import urllib2

class htmloutput():
    
    def __init__(self):
        self.datas = []
    
    
    def collection(self,data):
        if data is None:
            return 
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>'%data['url'].encode('utf-8'))
#==============================================================================
#             print data['title']
#==============================================================================
            fout.write('<td>%s</td>'%data['title'].encode('utf-8'))
            fout.write('<td>%s</td>'%data['summary'].encode('utf-8'))
            
            fout.write('</tr>')
        
        
        
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')