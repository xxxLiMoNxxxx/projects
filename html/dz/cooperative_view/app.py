from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Активируем CORS
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, async_mode='gevent', cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    emit('current_time', broadcast=True)

@socketio.on('video_event')
def handle_video_event(data):
    emit('video_event', data, broadcast=True)

@socketio.on('message')
def handle_message(msg):
    emit('message', msg, broadcast=True)

@app.route('/')
def index():
    return render_template('player.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
