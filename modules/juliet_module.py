from pygame import Rect

class module:
    mod_name = "unnamed_module"
    mod_id = -1
    mod_size = Rect(0,0,0,0)

    def __init__(self, _id = -1):
        print("Initializing generic module (This shouldn't happen...)")

    def draw(self, surf):
        "Takes a surface object and blits its data onto it"
        print("Draw call of generic module (This shouldn't happen...)")

    def update(self):
        "Update this module's internal state (do things like time updates, get weather, etc."
        print("Update call of generic module (This shouldn't happen...)")

def new_module(_id = -1):
    return module(_id)
