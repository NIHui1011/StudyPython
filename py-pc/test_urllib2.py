#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import cookielib

url = "http://www.baidu.com"

#第一种方法
print "第一种方法"
respose1 = urllib2.urlopen(url)
print respose1.getcode()
print len(respose1.read())


#第二种方法 伪装成浏览器去请求
print "第二种方法"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
respose2 = urllib2.urlopen(request)
print respose2.getcode()
print len(respose2.read())


#第三种方法
print "第三种方法"
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
respose3 = urllib2.urlopen(url)
print respose3.getcode()
print cj
print respose3.read()

