# -*- coding: utf-8 -*-
import urllib2
import re
import json
import string

APIKEY = 'e620ec2a512410c7a31f1b65e2a10e51'

def get_weather_info():
    url = "http://m.ip138.com/51/guangzhou/tianqi/"
    headers = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    req = urllib2.Request(url, headers=headers)
    opener = urllib2.urlopen(req)
    html = opener.read().decode('utf-8')
    rex = r'(?<=img src="/image/s[0-9].gif" alt=").{1,6}(?=" />)'
    rexx = r'(?<=div class="temperature">).{5,15}(?=</div>)'
    n = re.findall(rex, html)
    m = re.findall(rexx, html)
    str_wether = ""
    for (i, j) in zip(m, n):
        str_wether = str_wether + j + "  " + i + '\n'

    newcontent = "最近五天天气：\n" + str_wether.encode('utf-8')

    return newcontent


def get_news_info():
    url = 'http://apis.baidu.com/showapi_open_bus/channel_news/search_news?channelId=5572a109b3cdc86cf39001db&channelName=%E5%9B%BD%E5%86%85%E6%9C%80%E6%96%B0&title=%E4%B8%8A%E5%B8%82&page=1&needContent=0&needHtml=0'


    req = urllib2.Request(url)

    req.add_header("apikey", APIKEY)

    resp = urllib2.urlopen(req)
    content = resp.read()

    if(content):
        print(content)


def get_weixin_hot():
    url = 'http://apis.baidu.com/txapi/weixin/wxhot?num=10&rand=1&word=%E7%9B%97%E5%A2%93%E7%AC%94%E8%AE%B0&page=1&src=%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5'
    req = urllib2.Request(url)
    req.add_header("apikey", APIKEY)
    resp = urllib2.urlopen(req)
    content = resp.read()
    newcontent = json.loads(content)

    # 数据API返回的格式有误,需要调整
    news = []
    for aitem in newcontent['newslist']:
        del aitem['ctime']
        nitem = dict(zip(map(lambda x: string.lower(x), aitem.keys()), aitem.values()))
        news.append(nitem)

    return news
