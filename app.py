# -*- coding: utf-8 -*-
from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

#Add some randomness
now = datetime.datetime.now()
random.seed(now)

# list of cat subway stations
stops = [
    "Olleros",
    "José Hernández",
    "Juramento",
    "Congreso de Tucumán"
]

@app.route('/')
def index():

    station = random.choice(stops)
    print(station)
    return render_template('index.html', station=station)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
