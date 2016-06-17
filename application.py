# -*- coding: utf-8 -*-
import urllib2

import re
from flask import Flask, request, make_response, render_template
import hashlib
import xml.etree.ElementTree as ET
import time

app = Flask(__name__)


@app.route('/')
def index():
    print 'Hello'
    return render_template('first.html')

@app.route('/weixin', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = 'wodeweixintoken'
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s).hexdigest() == signature:
            # return render_template('first.html')
            return make_response(echostr)

    else:
        xml_rec = ET.fromstring(request.data)
        tousername = xml_rec.find("ToUserName").text
        fromusername = xml_rec.find("FromUserName").text
        content = xml_rec.find("Content").text
        msgTpye = xml_rec.find("MsgType").text
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"

        if content == u"天气":
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
            for (i,j) in zip(m,n):
                str_wether = str_wether + j + "  " + i + '\n'


            newcontent = "最近五天天气：\n" + str_wether.encode('utf-8')

            re_msg = (reply % (fromusername, tousername, str(int(time.time())), newcontent))
        return make_response(re_msg)

    print "Finished!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
