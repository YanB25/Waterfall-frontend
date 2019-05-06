#coding: utf-8
import threading
from flask import *
from flask_cors import CORS
import json
import time
import datetime
import calendar

app = Flask(__name__)

app.config['SECRET_KEY'] = 'WaterFall'

@app.route("/apis/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['currentUser'] = "admin"
        return json.dumps({
                "code" : 0,
                "data" : {
                    "username" : session['currentUser'],
                    "msg" : "logged in"
                }
            })
    if request.method == "GET":
        if 'currentUser' in session:
            return json.dumps({
                "code" : 0,
                "data" : {
                    "username" : session['currentUser'],
                    "msg" : "already logged in"
                }
            })
        else:
            return json.dumps({
                "code" : 1,
                "data" : {
                    "msg": "not logged in yet"
                }
            })


@app.route("/apis/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        session['currentUser'] = "admin"
        return json.dumps({
                "code" : 0,
                "data" : {
                    "username" : session['currentUser'],
                    "msg" : "logged in"
                }
            })
    if request.method == "GET":
        if 'currentUser' in session:
            return json.dumps({
                "code" : 0,
                "data" : {
                    "username" : session['currentUser'],
                    "msg" : "already logged in"
                }
            })
        else:
            return json.dumps({
                "code" : 1,
                "data" : {
                    "msg" :"not logged in yet"
                }
            })


@app.route('/apis/logout')
def logout():
    session.clear()
    return json.dumps({
        "code" : 0,
        "data" : {
            "msg" : "successfully logged out"
        }
    })

@app.route('/apis/username')
def username():
    if request.method == 'GET':
        name = request.args.get('username')
        if name == 'yanbin':
            return json.dumps({
                "code": 1,
                "data": {
                    "msg": "username already be used"
                }
            })
        return json.dumps({
            "code": 0,
            "data": {
                "msg": "username {} is available".format(name)
            }
        })

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True, port=8099, threaded=True)
    
