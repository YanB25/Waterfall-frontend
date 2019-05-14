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
                    "userid" : 0,
                    "msg" : "logged in"
                }
            })
    if request.method == "GET":
        if 'currentUser' in session:
            return json.dumps({
                "code" : 0,
                "data" : {
                    "username" : session['currentUser'],
                    "userid" : 0,
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
                    "userid" : 0,
                    "msg" : "logged in"
                }
            })
    if request.method == "GET":
        if 'currentUser' in session:
            return json.dumps({
                "code" : 0,
                "userid" : 0,
                "data" : {
                    "username" : session['currentUser'],
                    "userid" : 0,
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

@app.route('/apis/checkuser/<username>')
def checkuser(username):
    if request.method == 'GET':
        if username == 'yanbin':
            return json.dumps({
                "code": 1,
                "data": {
                    "msg": "username already be used"
                }
            })
        return json.dumps({
            "code": 0,
            "data": {
                "msg": "username {} is available".format(username)
            }
        })


@app.route('/apis/user/<userid>')
def userProfile(userid):
    if request.method == 'GET':
        if userid == 'undefined':
            return json.dumps({
                'code': 1
            })
        return json.dumps({
            "code": 0,
            "data": {
                "username": "username-for-{}".format(userid),
                "email": "user{}@mail2.sysu.edu.cn".format(userid),
                "phone": "13838383838",
                "balance": 23,
                "role": 0,
                "status": 0
            }
        })
    if request.method == 'POST':
        return json.dumps({
            "code": 0,
            "data": {
                "msg": "success"
            }
        })

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True, port=8099, threaded=True)
    
