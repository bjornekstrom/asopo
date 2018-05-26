from bs4 import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("")

asopo = BeautifulSoup(html_page, "html.parser")

for link in asopo.findAll('a', attrs={'href': re.compile("^http://")}):
    http = link.get('href')
    
    print http

for link in asopo.findAll('a', attrs={'href': re.compile("^https://")}):
    https = link.get('href')

    print https
