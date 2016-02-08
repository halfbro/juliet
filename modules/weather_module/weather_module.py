import juliet_module
from pygame import Rect
from time import time

from os import getcwd

class weather_module(juliet_module.module):
    mod_name = "weather_module"

    __last_update = time()
    __api = None

    def __init__(self, _id, _keyfile):
        print("Initializing Weather Module")
        self.mod_id = _id
        with open(_keyfile, 'r') as f:
            self.__api = f.read()

    def draw(self, surf):
        "Takes a surface object and blits its data onto it"
        print("Draw call of Weather Module")

    def update(self):
        "Update this module's internal state (do things like time updates, get weather, etc."
        # print("Update call of Weather Module")

def new_module(_id = -1, _keyfile = 'modules/weather_module/api.key'):
    return weather_module(_id, _keyfile)
