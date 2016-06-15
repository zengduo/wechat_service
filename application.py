from flask import Flask, request, make_response
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = 'vxoSJZUB7Qcj5lf6s4uLWIg'  
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
            
    else:
        xml_rec = ET.fromstring(request.data)
        ToUserName = xml_rec.find("ToUserName").text
        FromUserName = xml_rec.find("FromUserName").text
        Content = xml_rec.find("Content").text
        reply = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
        re_msg = (reply % (FromUserName, ToUserName, str(int(time.time())), Content))
        response = make_response(re_msg)
        response.content_type = 'application/xml'
        return response
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
