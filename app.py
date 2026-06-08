import flask
from flask import Flask
from optimize import optimize_all
import logging
import random
import glob

IMG_DIR = "images/optimized/"
IMG_DIR_FULL = f"./static/{IMG_DIR}"

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

optimize_all(app.logger)

def get_photos():
    return [IMG_DIR + _.split("/")[-1] for _ in glob.glob(f"{IMG_DIR_FULL}/*.webp")]

def choose_random_mainphoto():
    return random.choice([_ for _ in get_photos() if "main" in _])

@app.route("/")
def main():
    mainphoto = choose_random_mainphoto()
    photos = [_ for _ in get_photos() if _ != mainphoto]
    return flask.render_template("index.html", photos=photos, mainphoto=mainphoto)