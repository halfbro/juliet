import juliet_module
from pygame import Rect, font, draw
from time import time
import forecastio

weathericons = {
    'clear-day':'\uf00d',
    'clear-night':'\uf02e',
    'rain':'\uf019',
    'snow':'\uf01b',
    'sleet':'\uf0b5',
    'wind':'\uf050',
    'fog':'\uf0b6',
    'cloudy':'\uf013',
    'partly-cloudy-day':'\uf002',
    'partly-cloudy-day':'\uf086',
    'default':'\uf077',
}

class weather_module(juliet_module.module):
    mod_name = "weather_module"

    last_update = time()
    api = None
    forecast = None
    weather_font = None
    lat = None
    lng = None

    def __init__(self, _id, _keyfile, _lat, _lng):
        self.mod_id = _id
        self.lat = _lat
        self.lng = _lng
        self.weather_font = font.Font("weathericons.ttf",300)
        self.mod_rect = Rect((50,0), self.weather_font.size("\uf00d "))

        with open(_keyfile, 'r') as f:
            self.api = f.read()[:-1]

        forecastio.load_forecast(self.api, self.lat, self.lng, units = "us", callback=self.request_callback)

    def draw(self, surf):
        "Takes a surface object and blits its data onto it"
        if self.forecast:
            surface = self.weather_font.render(weathericons[self.forecast.daily().icon], True, (255,255,255))
            dirty = surf.blit(surface, (5,0))
            return dirty
        else:
            return Rect(0,0,0,0)

    def update(self):
        "Update this module's internal state (do things like time updates, get weather, etc."
        if self.last_update < time() - 3600:
            forecastio.load_forecast(self.api, self.lat, self.lng, units = "us", callback=self.request_callback)

    def request_callback(self, forecast):
        self.forecast = forecast
        self.last_update = time()
        self.changed = True

        print(self.forecast.daily().summary)
        print(self.forecast.json["timezone"])
        print(self.forecast.daily().icon)
        print(self.last_update)

def new_module(_id = -1, _keyfile = 'modules/weather_module/api.key', _lat = 40.7127, _lng = -74.0059):
    return weather_module(_id, _keyfile, _lat, _lng)
