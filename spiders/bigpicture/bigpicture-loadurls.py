import urllib2
import json
import lxml.html
from lxml import etree

def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_page_url(index):
	return 'http://bigpicture.ru/?paged='+str(index)

def get_post_images(page):
	html = lxml.html.fromstring(page)
	imgs = html.xpath('.//*[@class="content"]//p/a/img/@src')
	return imgs
	# for x in xrange(len(imgs)):
	# 	img = load_res(imgs[x])
	# 	f = open('/Users/tmshv/Desktop/architizer/a'+str(x), 'wb')
	# 	f.write(img)
	# 	f.close()

def get_blog_page_posts(index):
	url = get_page_url(index)
	html = lxml.html.fromstring(load_res(url))
	urls = html.xpath('.//*/div[@id="contentleft"]/h2/a/@href')
	return urls

urls = []
for x in xrange(1,10):
	print 'analyze', x, get_page_url(x)
	p = get_blog_page_posts(x)
	urls = urls + p

ufile = open('urls.txt', 'w')
ufile.write(json.dumps(urls))
ufile.close()