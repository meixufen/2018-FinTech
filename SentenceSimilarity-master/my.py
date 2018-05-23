# -*- coding:utf-8 -*-

import urllib, urllib2, sys
import ssl

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=P5zKovTywutlX2k2ZbGVrY3t&client_secret=fGc0aPRNqZMuk308byY2bbkilD12nl6E'
request = urllib2.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)