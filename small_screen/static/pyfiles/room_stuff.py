import Adafruit_DHT

def get_roomstuff():
    sensor = Adafruit_DHT.DHT22
    pin = 2
    h,t = Adafruit_DHT.read_retry(sensor, pin)

    return {"hum": f"Luftfeuchtigkeit: {round(h, 2)}", "temp": f"Raumtemperatur: {round(t, 2)}"}