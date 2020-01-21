from flask import Flask, render_template
from datetime import datetime
from static.pyfiles import weather, calendar
import json

with open("../config.json") as fp:
    file = json.load(fp)
    location = file["city"]

app = Flask(__name__)
TIME = datetime.now().strftime("%A, %d.%m.%Y")
CALANDER_EVENT_START = calendar.get_events()["start"][:5]
CALANDER_EVENT = calendar.get_events()["event"]
CALANDER_EVENT_END = calendar.get_events()["end"][:5]
CALANDER_EVENT_DT = calendar.get_events()["event_dt"]
PERIOD = f"{CALANDER_EVENT_START} - {CALANDER_EVENT_END}"


@app.route("/")
def index():
    return render_template("index.html", 
                            temp=weather.get_temp(), 
                            desc=weather.get_desc(), 
                            icon=weather.get_icon(), 
                            location=location, 
                            period=PERIOD,
                            event=CALANDER_EVENT,
                            event_date=CALANDER_EVENT_DT
                            )

if __name__ == "__main__":
    app.run(port=8080, debug=True)