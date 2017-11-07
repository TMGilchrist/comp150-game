import time
import random

import pygame

from Player import Player
from TestObject import PikachuStatue
from Attack import Swipe
from Enemy import ChaserEnemy
from Map import *
from Fog import Fog
from Invent import *

class Game:
    delta_time = 0  # time passed since last frame
    tick_time = 0   # time at the start of the frame, in seconds since
                    # the game started
    start_time = 0  # initial time.clock() value on startup (OS-dependent)
    t0 = time.time()
    screen = None   # PyGame screen
    objects = None  # list of active objects in the game
    player = None   # pointer to the player object
    map = None    # MapClass object
    quitting = False
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    def __init__(self):
        self.run()

    def run(self):
        """Runs the game -- game closes when this function ends.
           To be called on startup."""
        # Init Python
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,
                                               self.SCREEN_HEIGHT))

        # Init map
        self.map = MapClass()

        # Init fog
        self.fog = Fog()

        # Init character
        self.player = Player(0, 0)

        # Init inventory
        self.invent = Inventory()

        # Init objects and player
        self.objects = list()
        self.objects.append(self.player)  # player is always the first item

        # Add test Pikachi (Pikachodes?) (plural?)
        for i in xrange(10):
            self.objects.append(PikachuStatue(random.randint(0, 10),
                                              random.randint(0, 10)))
        # Add test sword
        self.objects.append(Swipe(3, 3))

        # Init test enemy at 5,5
        self.objects.append(ChaserEnemy(3, 3))

        # Init main game parameters
        self.start_time = time.clock()
        self.delta_time = 0.0

        # Main loop
        while not self.quitting:
            # Update timing
            last_time = self.tick_time
            self.tick_time = time.clock()

            self.delta_time = self.tick_time - last_time

            # Change day to true or false every #seconds, calls fog function to update surface
            seconds = 10
            t1 = time.time()
            dt = t1 - self.t0  # gets difference in start time and current time
            if dt >= seconds:
                self.fog.day = not self.fog.day
                self.t0 = t1  # resets timer variable
                self.fog.lift_fog()

            # Cap delta time to 10FPS to prevent gamebreaking bugs
            if self.delta_time >= 0.1:
                self.delta_time = 0.1

            # Perform PyGame event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and
                         event.key == pygame.K_ESCAPE):
                    self.quitting = True

            # Update objects (including player)
            for obj in self.objects:
                obj.update(self.delta_time, self.player, self.objects, None)

            # Render (todo: move into separate Render class?)
            self.screen.blit(self.map.img, (0, 0))

            for obj in self.objects:
                obj.render(self.screen)
            self.player.render(self.screen)

            # Render fog
            self.screen.blit(self.fog.surface, (self.player.x * MAP.TILE_SIZE - int(self.SCREEN_WIDTH*1.5 - self.player.sprite.get_width()/2),
                                                self.player.y * MAP.TILE_SIZE - int(self.SCREEN_HEIGHT*1.5 - self.player.sprite.get_height()/2)))

            # Update inventory
            self.invent.update()
            self.invent.render_invent(self.screen)

            # Splat to screen
            pygame.display.flip()

# Startup game!
Game()
