# -*- coding: utf-8 -*-

import hashlib
import web
import time
import os
import urllib2
import json
import urllib
import re
import random
import cookielib
from urllib import urlencode


url1 = "http://m.ip138.com/51/guangzhou/tianqi/"
headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
req = urllib2.Request(url1, headers=headers)
opener = urllib2.urlopen(req)
html = opener.read().decode('utf-8')
rex = r'(?<=img src="/image/s[0-9].gif" alt=").{1,6}(?=" />)'
rexx = r'(?<=div class="temperature">).{5,15}(?=/div>)'
n = re.findall(rex, html)
m = re.findall(rexx, html)

str_wether = ""
for (i, j) in zip(m, n):
    str_wether = str_wether + j + "    " + i + '\n'

# print str_wether
print "天气真晴朗\n" + str_wether.encode('utf-8')

# print html
# print n
# for littlen in n:
#     print littlen,
# print '\n'
# for littlem in m:
#     print littlem,
