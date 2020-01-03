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
    html_parser = json2html.convert(json=data)
    html_parser = html_parser.replace('<table border="1">', "<table class=container>")
    with open("./templates/data.html", "w") as f:
        f.write(html_parser)

    return render_template("index.html", title="OS Interface")