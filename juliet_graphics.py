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
        pygame.time.wait(1000)
        clock = pygame.time.Clock()

        self.current_modules.append(juliet_importer.modules['text_module'].new_module(1,"Hello World!"))
        self.current_modules.append(juliet_importer.modules['text_module'].new_module(2,"This is juliet"))
        self.current_modules.append(juliet_importer.modules['text_module'].new_module(3,"A method for displaying information on a mirror"))
        self.current_modules.append(juliet_importer.modules['text_module'].new_module(5,"TEST"))
        self.current_modules.append(juliet_importer.modules['fps_module'].new_module(7,clock))
        self.current_modules.append(juliet_importer.modules['weather_module'].new_module(8))

        while not self.stop_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_q:
                    self.stop();

            dirty_rects = []

            # Update modules first - they may change in size
            for module in self.current_modules:
                module.update()
                if module.changed:
                    dirty_rects.append(module.mod_rect.copy())
                    module.changed = False

            # Resolve any module collisions by shifting older modules down
            '''
            mods = self.current_modules
            for a in range(len(mods)):
                for b in range(a+1,len(mods)):
                    if mods[a].mod_rect.colliderect(mods[b].mod_rect):
                        dirty_rects.append(mods[b].mod_rect.copy())
                        mods[b].mod_rect.move_ip(0, (mods[a].mod_rect.bottom - mods[b].mod_rect.top)**(1.7)/100+1)
                        mods[b].mod_rect.clamp_ip(self.screen.get_rect())
                        dirty_rects.append(mods[b].mod_rect.copy())
            '''
            # Alternatively don't move modules and let them overlap
            for a in self.current_modules:
                dirty_rects.append(a.mod_rect.copy())
                a.mod_rect.clamp_ip(self.screen.get_rect())
                dirty_rects.append(a.mod_rect.copy())
            
            # Draw functions done here
            # This is one method - union all the dirty rectangles, then check if any module overlaps the dirty area.
            # This means that the module must be redrawn
            '''
            if dirty_rects:
                dirty_r = dirty_rects[0]
                dirty_r.unionall_ip(dirty_rects)
                self.screen.fill(BLACK, dirty_r)
                for module in self.current_modules:
                    if module.mod_rect.colliderect(dirty_r):
                        module.draw(self.screen.subsurface(module.mod_rect.clip(self.screen.get_rect())))
                #pygame.draw.rect(self.screen, (255,255,200), dirty_r, 1)

                pygame.display.update(dirty_r)
            '''
            # Alternate implementation: loop through all the modules and check if they collide with any of the dirty
            # rectangles in dirty_rects. If colliding, redraw. Works best on small number of modules
            
            for dirty in dirty_rects:
                self.screen.fill(BLACK,dirty)

            for module in self.current_modules:
                if module.mod_rect.collidelistall(dirty_rects):
                    self.screen.fill(BLACK, module.mod_rect)
                    module.draw(self.screen.subsurface(module.mod_rect.clip(self.screen.get_rect())))

            for dirty in dirty_rects:
                pygame.display.update(dirty)
            

            # Need some kind of method for instantiating new modules
            # Probably by calling some kind of method so its decoupled from the CLI module

            # Also some way for dealing with overlaps of module boxes
            # So some kind of way of having a list of all module boxes

            clock.tick(60)



# For testing porpoises only
graphics = juliet_graphics();
graphics.start();
graphics.join();
