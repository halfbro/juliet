import juliet_module
from pygame import Rect, font, draw

class text_module(juliet_module.module):
    mod_name = "text_module"
    mod_id = -1
    mod_rect = Rect(0,0,0,0)
    changed = False

    module_font = None
    text = None

    def __init__(self, _id, init_text):
        self.mod_id = _id
        self.text = init_text
        self.module_font = font.Font("Comme-Thin.ttf", 50)
        self.mod_rect = Rect((0,0), self.module_font.size(self.text)).inflate(10,0)

    def draw(self, surf):
        "Draw this module to the surface provided. Returns a Rect of the affected area"
        text_surface = self.module_font.render(self.text, True, (255,255,255))
        dirty = surf.blit(text_surface, (5,0))
        draw.rect(surf, (255,255,255), surf.get_rect(), 4)
        return dirty

    def update(self):
        "This module's text cannot be updated"

def new_module(_id, text = "..."):
    return text_module(_id, text)
