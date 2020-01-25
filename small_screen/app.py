from flask import Flask, render_template
from static.pyfiles import weather, calendar
import json

CALANDER_EVENT_START = calendar.get_events()["start"][:5]
CALANDER_EVENT = calendar.get_events()["event"]
CALANDER_EVENT_END = calendar.get_events()["end"][:5]
CALANDER_EVENT_DT = calendar.get_events()["event_dt"]
PERIOD = f"{CALANDER_EVENT_START} - {CALANDER_EVENT_END}"

with open("../config.json") as fp:
    file = json.load(fp)
    location = file["city"]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calendar")
def calendar_route():
    return render_template("calendar.html",
                            event_date = CALANDER_EVENT_DT,
                            period = PERIOD,
                            event = calendar.get_events()["event"]
                            )

@app.route("/weather")
def weather_route():
    return render_template("weather.html", location=location, temp=weather.get_temp())

@app.route("/animation")
def animation():
    return render_template("animation.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)