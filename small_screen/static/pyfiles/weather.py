import requests
import json

with open("../config.json") as fp:
    file = json.load(fp)
    APIKEY = file["ApiKey"]
    CITY = file["city"]
    LOCATION = file["country"]

UNIT = "metric"
BASEURL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY},{LOCATION}&APPID={APIKEY}&units={UNIT}"


result = requests.get(BASEURL).json()

def get_temp():
    return result["main"]["temp"]

def get_desc():
    return result["weather"][0]["main"]

def get_icon():
    icon = result["weather"][0]["icon"]
    icons = {
        "01d": "static/img/clear_sky.png",
        "01n": "static/img/clear_sky.png",
        "02d": "static/img/few_clouds.png",
        "02n": "static/img/few_clounds.png",
        "03d": "static/img/clouds.png",
        "03n": "static/img/clouds.png",
        "04d": "static/img/broken_clouds.png",
        "04n": "static/img/broken_clouds.png",
        "09d": "static/img/shower_rain.png", 
        "09n": "static/img/shower_rain.png",
        "10d": "static/img/rain.png",
        "10n": "static/img/rain.png",
        "11d": "static/img/thunderstorm.png",
        "11n": "static/img/thunderstorm.png",
        "13d": "static/img/snow.png",
        "13n": "static/img/snow.png",
        "50d": "static/img/fog.png",
        "50n": "static/img/fog.png"
    }

    return icons[icon]