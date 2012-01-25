import urllib2
import json
import lxml.html
from lxml import etree

def load_res(url):
	res = urllib2.urlopen(url)
	return res.read()

def get_post_images(page_url):
	page = load_res(page_url)
	html = lxml.html.fromstring(page)
	img_smalls = html.xpath('.//div[@class="post_content"]/div/a/img/@src')
	img_pages = html.xpath('.//div[@class="post_content"]/div/a/@href')
	img_bigs = get_big_image_url_list(img_pages)

	images= []
	for x in xrange(len(img_pages)):
		images.append({'small': img_smalls[x], 'big': img_bigs[x], 'page': page_url})
	return images

def get_big_image_url_list(page_url_list):
	imgs = []
	for x in xrange(len(page_url_list)):
		page_url = page_url_list[x]
		page = load_res(page_url)
		html = lxml.html.fromstring(page)
		print 'get big from', page_url
		try:
			img = html.xpath('.//*[@id="download_image"]/a/@href')[0]
			imgs.append(img)
		except IndexError, e:
			print 'ALERT: load big image warning:', page_url
			imgs.append(page_url)
		
	return imgs

ufile = open('urls.txt', 'r')
posts = json.loads(ufile.read())
ufile.close()

imgs = []
for x in xrange(len(posts)):
	url = posts[x]['url']
	print 'analyze page index', x, url
	i = get_post_images(url)
	imgs = imgs + i

print 'compeled'
print len(imgs)
print imgs

imgfile = open('imgs.txt', 'w')
imgfile.write(json.dumps(imgs))
imgfile.close()