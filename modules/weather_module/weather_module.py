import juliet_module
from pygame import Rect
from time import time
import forecastio

class weather_module(juliet_module.module):
    mod_name = "weather_module"

    __last_update = time()
    __api = None
    __forecast = None

    def __init__(self, _id, _keyfile):
        print("Initializing Weather Module")
        self.mod_id = _id
        with open(_keyfile, 'r') as f:
            self.__api = f.read()[:-1]

        lat = 40.7127
        lng = 74.0059
        forecastio.load_forecast(self.__api, lat, lng, units = "us", callback=self.request_callback)

    def draw(self, surf):
        "Takes a surface object and blits its data onto it"
        print("Draw call of Weather Module")

    def update(self):
        "Update this module's internal state (do things like time updates, get weather, etc."
        # print("Update call of Weather Module")

    def request_callback(self, forecast):
        self.__forecast = forecast
        print(self.__forecast.daily().summary)

def new_module(_id = -1, _keyfile = 'modules/weather_module/api.key'):
    return weather_module(_id, _keyfile)
