from flask import Flask, redirect
from flask import render_template
from flask import request
import string
import random
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route("/")
def cocokua_home():
	return render_template('index.html')

@app.route('/i_<video>_n_<room>/')
def cocokua_invite(video, room):
        return render_template('index.html')

@app.route('/c_<video>_n_<room>/')
def cocokua_create(video, room):
        return render_template('index.html')

@app.route('/r_<video>_n_<room>/')
def cocokua_room(video, room):
        return render_template('room.html', v=video, r=room)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)

