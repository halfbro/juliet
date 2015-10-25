import juliet_module
from pygame import Rect, font, draw

class text_module(juliet_module.module):
    mod_name = "text_module"
    mod_id = -1
    mod_size = Rect(0,0,0,0)

    module_font = None
    text = "Hello World!"

    def __init__(self, _id):
        self.mod_id = _id
        self.mod_size = Rect(0,0,720,100)
        self.module_font = font.Font("Comme-Thin.ttf", 100)

    def draw(self, surf):
        text_surface = self.module_font.render(self.text, True, (255,255,255))
        dirty = surf.blit(text_surface, (0,-30))
        draw.rect(surf, (255,255,255), surf.get_rect(), 4)
        return dirty

    def update(self):
        "Update this module's internal state (do things like time updates, get weather, etc."
        print("Update call of text module")

def new_module(_id):
    return text_module(_id)
