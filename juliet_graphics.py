import os;
import pygame;
from threading import Thread;
import juliet_importer;

BLACK = (0,0,0);
WHITE = (255,255,255);

class juliet_graphics (Thread):
    screen = None
    current_modules = []
    stop_running = False

    def __init__(self):
        Thread.__init__(self)
        self.stop_running = False

        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    print('Driver: {0} failed.'.format(driver))
                    continue
                found = True
                break

        if not found:
            raise Exception('Graphics: No suitable video driver found!')

        displayinfo = pygame.display.Info()
        size = (displayinfo.current_w, displayinfo.current_h)
        print("Framebuffer size: %d x %d" % (size[0], size[1]))

        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)

        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        self.screen.fill(BLACK)
        pygame.display.update()

    def stop(self):
        self.stop_running = True

    def run(self):
        self.current_modules.append(juliet_importer.modules['text_module'].new_module(1))
        self.current_modules.append(juliet_importer.modules['text_module'].new_module(2))
        dirty_rects = []
        while not self.stop_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_q:
                    self.stop();

            # Implement draw function here
            for module in self.current_modules:
                position = module.mod_size.move(40,105*module.mod_id)
                dirty_rects.append(position)
                module.draw(self.screen.subsurface(position))

            for dirty in dirty_rects:
                pygame.display.update(dirty.inflate(20,20))
                dirty_rects.remove(dirty)

            self.screen.fill(BLACK)

            # Need some kind of method for instantiating new modules

            # Also some way for dealing with overlaps of module boxes
            # So some kind of way of having a list of all module boxes

            pygame.time.wait(10)


# For testing porpoises only
graphics = juliet_graphics();
graphics.start();
graphics.join();
