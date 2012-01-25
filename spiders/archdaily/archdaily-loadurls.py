import urllib2
import json
import lxml.html
from lxml import etree

def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_blog_page_posts(index):
	url = 'http://www.archdaily.com/page/'+str(index)
	html = lxml.html.fromstring(load_res(url))
	urls = html.xpath('.//*[@class="post"]/div/h2/a/@href')
	dates1 = html.xpath('.//*[@class="post"]/div[@class="post_date"]/div[position()=1]/text()')
	dates2 = html.xpath('.//*[@class="post"]/div[@class="post_date"]/div[position()=2]/text()')
	posts = []
	for x in xrange(len(urls)):
		date = dates1[x] + ' ' + dates2[x]
		posts.append({'url':urls[x], 'date':date})
	return posts

urls = []
# 596
for x in xrange(1, 596):
	print 'analyze', x
	p = get_blog_page_posts(x)
	urls = urls + p

ufile = open('urls.txt', 'w')
ufile.write(json.dumps(urls))
ufile.close()
# print get_blog_page_posts(40)