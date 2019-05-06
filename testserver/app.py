#coding: utf-8
import threading
from flask import *
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
                "data" : "not logged in yet"
            })

@app.route('/apis/logout')
def logout():
    session.clear()
    return json.dumps({
        "code" : 0,
        "data" : "successfully logged out"
    })

if __name__ == '__main__':
    app.run(debug=True, port=8099, threaded=True)
    
