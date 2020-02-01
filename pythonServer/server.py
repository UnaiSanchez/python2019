from flask import Flask, render_template, request
from asdf import asdf
from user import User
from dog_generator import dog_generator
app = Flask(__name__)
users = set()
@app.route("/index.html")
def index():
    return "Esto es el mejor servidor de python del mundo"
@app.route("/login")
def login():
    return render_template("login.html",bg_colour="cyan", url="/unai/pythonServer/login-data")
@app.route("/login-data")
def login_dat():
    for user in users:
        if request.args.get("username") == user.name:
            if asdf(request.args.get("password"))== asdf(user.password):
                return "Nice"
        return "Nope"


@app.route("/doggos")
def doggos():
    return render_template("dogs.html")
@app.route("/dog_url_dont_open")
def hidden_dog_function():
    next_data= next(dog_generator)
    del next_data["fileSizeBytes"]
    if next_data["url"].endswith("mp4") or next_data["url"].endswith('webm'):
        next_data["type"] = 'video'
    else:
        next_data["type"] = "image"
    return next_data


def create_user(name,password):
    user = User(name, password)
    users.add(user)

import sys
print(sys.argv)
if "--port" in sys.argv:
    try:
        port = int(sys.argv[sys.argv.index("--port")+1])
    except ValueError:
        print("ivalid port number")
else:
    print("no port argument")
import os
os.system("python3 python-server/create_htaccess.py --port {}".format(port))
create_user("Unai","passowrd")
app.run(host = "0.0.0.0", port = port )