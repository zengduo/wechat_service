from flask import Flask, request, make_response


app = Flask(__name__)

DEBUG = True

@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = 'vxoSJZUB7Qcj5lf6s4uLWIg'
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp. nonce, token]
        s.sort()
        s = ''.join(s)
        if signature == hashlib.sha1(s).hexdigest():
            return make_response(echostr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
