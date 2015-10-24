import math;
import os;
import pygame;
import sys;
import time;
from threading import Thread;
import juliet_importer;

BLACK = (0,0,0);
WHITE = (255,255,255);

class juliet_graphics (Thread):
    screen = None;
    stop_running = False;

    def __init__(self):
        Thread.__init__(self);
        self.stop_running = False;

        drivers = ['fbcon', 'directfb', 'svgalib'];
        found = False;
        for driver in drivers:
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver);
                try:
                    pygame.display.init()
                except pygame.error:
                    print 'Driver: {0} failed.'.format(driver);
                    continue;
            found = True;
            break;

        if not found:
            raise Exception('Graphics: No suitable video driver found!');

        displayinfo = pygame.display.Info();
        size = (displayinfo.current_w, displayinfo.current_h);
        print "Framebuffer size: %d x %d" % (size[0], size[1]);

        pygame.init();
        pygame.font.init();
        pygame.mouse.set_visible(False);

        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN);
        self.screen.fill(BLACK);
        pygame.display.update();

    def stop(self):
        self.stop_running = True;

    def run(self):
        while not self.stop_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_q:
                    self.stop();


# For testing porpoises only
graphics = juliet_graphics();
graphics.start();
graphics.join();
