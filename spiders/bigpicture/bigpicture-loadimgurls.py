import urllib2
import json
import lxml.html
from lxml import etree

def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_post_images(page):
	html = lxml.html.fromstring(page)
	return html.xpath('.//div[@id="inkontent"]/div[substring-before(@id, "_")="attachment"]/img/@src')

ufile = open('urls.txt', 'r')
posts = json.loads(ufile.read())
ufile.close()

imgs = []
for x in xrange(len(posts)):
	url = posts[x]
	print 'analyze', x, url
	# print url
	page = load_res(url)
	i = get_post_images(page)
	imgs.append({
		'post': url
		'imgs': i
	})

imgfile = open('imgs.txt', 'w')
imgfile.write(json.dumps(imgs))
imgfile.close()

	# for x in xrange(len(imgs)):
	# 	img = load_res(imgs[x])
	# 	f = open('/Users/tmshv/Desktop/architizer/a'+str(x), 'wb')
	# 	f.write(img)
	# 	f.close()