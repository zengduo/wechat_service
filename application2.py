# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, render_template
from wechat_sdk import WechatBasic, WechatConf, WechatExt
from wechat_sdk.messages import TextMessage, ImageMessage, VideoMessage, LocationMessage, LinkMessage, EventMessage, \
    VoiceMessage
from wechat_sdk.exceptions import ParseError
from plugins import get_weather_info, get_weixin_hot

conf = WechatConf(
    token='zengduo',
    appid='wx297cc5cbd1a04a39',
    encrypt_mode='normal',
)

app = Flask(__name__)

wechat = WechatBasic(conf=conf)

answer = u'<a href="%s">【点击这里查看更多新闻】</a>\n\n欢迎使用'


@app.route('/')
def hello():
    return render_template('first.html')


@app.route('/test')
def test():
    return render_template('first.html')


@app.route('/weixin', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        print "GET"
        query = request.args
        signature = query.get("signature", "")
        timestamp = query.get("timestamp", "")
        nonce = query.get("nonce", "")
        echostr = query.get("echostr", "")

        if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
            return make_response(echostr)
        else:
            print "wrong!"
    else:
        try:
            wechat.parse_data(request.data)
        except ParseError:
            return

        # 事件消息类
        if isinstance(wechat.message, EventMessage):
            if wechat.message.type == 'subscribe':
                content = "Hello World!"
                return wechat.response_text(content)

            elif wechat.message.type == 'location':
                latitude = wechat.message.latitude
                longitude = wechat.message.longitude
                precision = wechat.message.precision
                content = "nice"
                return wechat.response_text(content)

            else:
                content = "Hello World!"
                print "someone has off"
                return wechat.response_text(content)

        # 文本消息类
        if isinstance(wechat.message, TextMessage):
            content = wechat.message.content
            if content == u'天气':
                weatherinfo = get_weather_info()
                return wechat.response_text(weatherinfo, escape=False)

            if content == u'网页':
                url = 'http://f7cf5b0.ngrok.natapp.cn/test'
                content = answer % url
                return wechat.response_text(content)

            if content == u'新闻':
                articles = get_weixin_hot()
                return wechat.response_news(articles)

            if content == u'买':
                content = 'https://detail.tmall.com/item.htm?id=41620925543&ali_refid=a3_430583_1006:1109914468:N:3m%E5%8F%A3%E7%BD%A9:3b38f1a5c4c751847125a4ef56fe8a68&ali_trackid=1_3b38f1a5c4c751847125a4ef56fe8a68'
                return wechat.response_text(content)


            else:
                return wechat.response_text(content)

        else:
            content = "功能尚未开放，请耐心等待"
            return wechat.response_text(content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
