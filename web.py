from flask import Flask
from flask import render_template
from osquery_handler import send_and_receive_all
from json2html import *
from flask import render_template


#global variable
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style" : "width:100%"}

app = Flask(__name__)

@app.route("/")
def hello():
    data = send_and_receive_all()

    with open("./templates/index.html", "w") as f:
        f.write(json2html.convert(json = data))

    return render_template("index.html")