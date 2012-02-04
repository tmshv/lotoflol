import urllib2
import json
import lxml.html
from lxml import etree

def get_post_images(page):
	html = lxml.html.fromstring(page)
	imgs = html.xpath('.//*[@class="content"]//p/a/img/@src')
	return imgs

ufile = open('imgs.txt', 'r')
imgs = json.loads(ufile.read())
ufile.close()

print len(imgs)