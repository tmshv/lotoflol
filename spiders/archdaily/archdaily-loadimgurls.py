import urllib2
import json
import lxml.html
from lxml import etree

def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_post_images(page):
	html = lxml.html.fromstring(page)
	imgs = html.xpath('.//*[@class="content"]//p/a/img/@src')
	return imgs

ufile = open('urls.txt', 'r')
posts = json.loads(ufile.read())
ufile.close()

imgs = []
for x in xrange(len(posts)):
	print 'analyze', x
	url = posts[x]['url']
	page = load_res(url)
	i = get_post_images(page)
	imgs = imgs + i

imgfile = open('imgs.txt', 'w')
imgfile.write(json.dumps(imgs))
imgfile.close()

	# for x in xrange(len(imgs)):
	# 	img = load_res(imgs[x])
	# 	f = open('/Users/tmshv/Desktop/architizer/a'+str(x), 'wb')
	# 	f.write(img)
	# 	f.close()