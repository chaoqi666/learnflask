from flask import Flask,render_template
from models import User
app = Flask(__name__)

@app.route('/')
def hello_world():
    content = "hello world"
    return render_template('index.html',content=content)

@app.route('/user')
def user_index():
    user1 = User(1,'qc')
    return render_template('user_index.html',user=user1)

@app.route('/query_user/<user_id>')
def query_user(user_id):
    user2 = None
    if int(user_id) == 1:
        user2 = User(1,'qc')

    return render_template('user_id.html',user=user2)

@app.route('/users')
def user_list():
    users = []
    for i in range(1,11):
        user = User(i,'admin'+str(i))
        users.append(user)

    return render_template('user_list.html',users=users)

@app.route('/one')
def one_base():
    return render_template('one_base.html')

@app.route('/two')
def two_base():
    return render_template('two_base.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)


