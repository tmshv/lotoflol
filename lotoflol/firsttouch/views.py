# Create your views here.
import re
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
import json
from random import randint

def first_hello(request):
    #t = get_template('justfile')
    #return HttpResponse(t)
    
    furls = open('/home/py/Dropbox/Py.com/architizer-imgs.txt', 'r')
    urls = json.loads(furls.read())
    furls.close()
    
    showed_urls = []
    for i in xrange(10):
        url = urls[randint(0, len(urls))]
        showed_urls.append({'url': url})
        
    variables = Context({
    	'urls': showed_urls
	})
    
    tmp = get_template('simple_stream.html')
    res = tmp.render(variables)
    
    return HttpResponse(res)
    #return HttpResponse('first lol words')

def get_feed(request, site):
    file = '/home/py/lotofLOL/feed/<site>/rss.xml'
    file = re.sub('<site>', site, file)
    rssfile = open(file, 'r')
    feed = rssfile.read()
    rssfile.close()

    return HttpResponse(feed)
    #return HttpResponse('first lol words')