import juliet_module
from pygame import Rect, font

class fps_module(juliet_module.module):
    mod_name = "text_module"

    module_font = None
    clock = None
    text = None

    def __init__(self, _id, _clock):
        self.mod_id = _id
        self.clock = _clock
        self.module_font = font.Font("Comme-Thin.ttf", 25)
        self.mod_rect = Rect((0,0), self.module_font.size("FPS: ")).inflate(6,0)

    def draw(self, surf):
        "Write FPS to the screen"
        text_surface = self.module_font.render(self.text, True, (255,255,255))
        dirty = surf.blit(text_surface, (3,0))
        return dirty

    def update(self):
        "This module's text cannot be updated"
        fps = self.clock.get_fps()
        self.text = "FPS: {:.1f}".format(fps)
        self.mod_rect = Rect((0,1040), self.module_font.size("FPS: {:.1f}".format(fps))).inflate(6,0)
        self.changed = True

def new_module(_id, _clock):
    return fps_module(_id, _clock)
