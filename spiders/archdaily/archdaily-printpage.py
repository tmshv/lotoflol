import urllib2
import json
import lxml.html
from lxml import etree

ufile = open('urls.txt', 'r')
urls = json.loads(ufile.read())
ufile.close()

print len(urls)