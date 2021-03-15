# from datetime import datetime
from flask import Flask, render_template
import sys, os
# from . import app
from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

# Some configuration, ensures
# 1. Pages are loaded on request.
# 2. File name extension for pages is Markdown.
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name)

# URL Routing - Flat Pages
# Retrieves the page path and
@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("hello_there_2.html", page=page)

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")

# Main Function, Runs at http://0.0.0.0:8000
# Modified Main
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)

# https://macfire.github.io/devops16/html/devops16_6_deploy_flask_app_w_git.html
# https://dev.to/lordofdexterity/deploying-flask-app-on-heroku-using-github-50nh
# https://www.freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221/



