from flask import Flask, render_template, request, session, make_response
from flask_sockets import Sockets
#import json
#import yaml
#import traceback

app = Flask('pp')
app.debug = True
app.secret_key = 'secret'
socket = Sockets(app)

sockets = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/post", methods=["POST", "GET"])
def post():
    secret = request.args.get("secret")
    if secret != "supersecretkey":
        return "no thanks!";

    msg = request.args.get('msg')

    try:
        for ws in sockets:
            ws.send(msg)
    except Exception as e:
        print("Error!")
        print(e)

    return "thanks!"

@socket.route('/stream')
def stream(ws):
    sockets.append(ws)
    print("connected!")
    while True:
        msg = ws.receive()







