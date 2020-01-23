from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/weather")
def weather():
    return render_template("weather.html")

if __name__ == "__main__":
    app.run(port=8080, debug=True)