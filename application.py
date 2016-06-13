from flask import Flask, request, make_response


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
# def wechat_auth():
#     if request.method == 'GET':
#         token = ''
#         query = request.args
#         signature = query.get('signature', '')
#         timestamp = query.get('timestamp', '')
#         nonce = query.get('nonce', '')
#         echostr = query.get('echostr', '')
#         s = [timestamp. nonce, token]
#         s.sort()
#         s = ''.join(s)
#         if signature == hashlib.sha1(s).hexdigest():
#             return make_response(echostr)
def hello():
    return '<p>Hello World!</p>'

if __name__ == '__main__':
    app.run(debug=True)
