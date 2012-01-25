import urllib2
import json
import lxml.html
from lxml import etree

url = 'http://www.architizer.com/en_us/blog/dyn/37002/infrared-hong-kong/'
def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()

page = load_res(url)

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
	url = 'http://www.architizer.com/en_us/blog/page/'+str(index)
	html = lxml.html.fromstring(load_res(url))
	urls = html.xpath('.//*[@class="post"]/h2/a/@href')
	dates = html.xpath('.//*[@class="post"]/p/text()')
	posts = []
	for x in xrange(len(urls)):
		posts.append({'url':urls[x], 'date':dates[x]})
	return posts

urls = []
for x in xrange(1,223):
	print 'analyze', x
	p = get_blog_page_posts(x)
	urls = urls + p

ufile = open('urls.txt', 'w')
ufile.write(json.dumps(urls))
ufile.close()

# xml = etree.XML(page)
# print xml.xpath('/html')
# print xml.xpath('div/(@class == content)')