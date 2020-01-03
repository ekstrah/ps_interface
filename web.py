from flask import Flask
from flask import render_template
from osquery_handler import process_by_username, process_by_cpu_from_bootup, process_by_memory
from json2html import *
from flask import render_template


#global variable
build_direction = "LEFT_TO_RIGHT"
table_attributes = {"style" : "width:100%"}

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", title="OS Index")
    # return render_template("index.html")

@app.route("/general")
def general():
    data = process_by_username()
    html_parser = json2html.convert(json=data)
    html_parser = html_parser.replace('<table border="1">', "<table class=container>")
    with open("./templates/data_main.html", "w") as f:
        f.write(html_parser)

    return render_template("general.html", title="OS Interface")

@app.route("/cpu_intensive")
def cpu_intensive():
    data = process_by_cpu_from_bootup()
    html_parser = json2html.convert(json=data)
    html_parser = html_parser.replace('<table border="1">', "<table class=container>")
    with open("./templates/data_cpu.html", "w") as f:
        f.write(html_parser)

    return render_template("cpu.html", title="OS Interface CPU")

@app.route("/memory_intensive")
def memory_intensive_intensive():
    data = process_by_memory()
    html_parser = json2html.convert(json=data)
    html_parser = html_parser.replace('<table border="1">', "<table class=container>")
    with open("./templates/data_mem.html", "w") as f:
        f.write(html_parser)

    return render_template("mem.html", title="OS Interface Memory")