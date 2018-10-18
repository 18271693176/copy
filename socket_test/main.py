import os
from flask import Flask,render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app, async_mode='gevent')
app.config['SECRET_KEY'] = os.urandom(12).encode('hex')



@app.route('/')
def index():

    socketio.emit('ping event', {'data': 42}, namespace='/chat',room=123)
    return render_template('/index.html')

# @app.route('/')
# def ping():
#     socketio.emit('ping event', {'data': 42}, namespace='/chat')


if __name__ == '__main__':
    app.run(debug=True)

