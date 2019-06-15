from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello,World"

@app.route('/user',methods = ['POST'])
def hello_user():
    return "hello,user"

@app.route('/users/<id>')
def hello_id(id):
    return "hello users:"+id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return "query user:"+id

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True,threaded=True)