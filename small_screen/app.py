from flask import Flask, render_template
from static.pyfiles import weather
import json

with open("../config.json") as fp:
    file = json.load(fp)
    location = file["city"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/weather")
def weather_route():
    return render_template("weather.html", location=location, temp=weather.get_temp())

@app.route("/animation")
def animation():
    return render_template("animation.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)