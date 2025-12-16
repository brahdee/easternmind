import flask
from flask import Flask
import glob

IMG_DIR = "./static/images"

app = Flask(__name__)

def get_photos():
    return ["images/" + _.split("/")[-1] for _ in glob.glob(f"{IMG_DIR}/*.jpg")]

@app.route("/")
def main():
    return flask.render_template("index.html", photos=get_photos())