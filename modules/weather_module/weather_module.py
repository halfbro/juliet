import juliet_module
from pygame import Rect, font, draw
from time import time
import forecastio

class weather_module(juliet_module.module):
    mod_name = "weather_module"

    __last_update = time()
    __api = None
    __forecast = None
    __weather_font = None
    __lat = 40.7127
    __lng = -74.0059

    def __init__(self, _id, _keyfile):
        print("Initializing Weather Module")
        self.mod_id = _id
        self.__weather_font = font.Font("weathericons.ttf",400)
        self.mod_rect = Rect((300,50), self.__weather_font.size("\uf00d "))

        with open(_keyfile, 'r') as f:
            self.__api = f.read()[:-1]

        forecastio.load_forecast(self.__api, self.__lat, self.__lng, units = "us", callback=self.request_callback)

    def draw(self, surf):
        "Takes a surface object and blits its data onto it"
        surface = self.__weather_font.render("\uf00d", True, (255,255,255))
        dirty = surf.blit(surface, (5,0))
        return dirty

    def update(self):
        "Update this module's internal state (do things like time updates, get weather, etc."
        # print("Update call of Weather Module")

    def request_callback(self, forecast):
        self.__forecast = forecast
        print(self.__forecast.daily().summary)
        print(self.__forecast.json["timezone"])
        print(self.__forecast.daily().icon)
        print(self.__last_update)

def new_module(_id = -1, _keyfile = 'modules/weather_module/api.key'):
    return weather_module(_id, _keyfile)
