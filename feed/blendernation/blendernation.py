import urllib2
import json
import lxml.html
from lxml import etree
# import feedparser

def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()#.decode('UTF-8')

def get_full_post(page_url):
	'get_full_post', page_url
	page = load_res(page_url)
	html = lxml.html.fromstring(page)
	content = html.xpath('.//div[@class="entry-content"]')[0]
	post = content.xpath('//div[@id="content"]/article/div[@class="entry-content"]/div[@class="sociable"]/preceding-sibling::*')
	post = post[:len(post)-2]
	a = lxml.html.fromstring('<div></div>')
	for x in xrange(len(post)):
		a.append(post[x])
	return etree.tostring(a)#, encoding='UTF-8')#, xml_declaration=False)

url = 'http://feeds.feedburner.com/Blendernation'
rss = load_res(url)
feed = etree.fromstring(rss)

items = feed.xpath('//item')
for x in xrange(len(items)):
	d = items[x].xpath('./description')[0]
	link = items[x].xpath('./link')[0].text
	d.text = get_full_post(link)

# print etree.tostring(feed, encoding='UTF-8', xml_declaration=False)
open('rss.xml', 'w').write(etree.tostring(feed))#, encoding='UTF-8', xml_declaration=False))

# print get_full_post('http://www.blendernation.com/2012/01/23/redefining-3d-typography-and-designing-3d-type-in-blender')
# print get_full_post('http://feedproxy.google.com/~r/Blendernation/~3/jWJ8wHzeeLk/')