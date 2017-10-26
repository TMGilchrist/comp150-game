import time
import random

import pygame

from Player import Player
from TestObject import PikachuStatue

class Game:
    delta_time = 0  # time passed since last frame
    tick_time = 0  # time at the start of the frame, in seconds since the game started
    screen = None  # pygame screen
    objects = None  # list of active objects in the game
    player = None  # pointer to the player object
    quitting = False
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480

    def __init__(self):
        self.run()

    def run(self):
        # Init Python
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # Init character
        self.player = Player(0, 0)

        # Init Objects
        self.objects = list()
        for i in xrange(10):
            self.objects.append(PikachuStatue(random.randint(0, 10), random.randint(0, 10)))

        # Init main game parameters (todo: split all this into a class, no globals)
        self.tick_time = time.clock()  # time at the beginning of the current game tick
        self.delta_time = 0.0

        # Main loop
        running = True
        while running:
            # Update timing
            last_time = self.tick_time
            self.tick_time = time.clock()

            self.delta_time = self.tick_time - last_time

            # Perform PyGame event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and
                         event.key == pygame.K_ESCAPE):
                    running = False

            # Update player and objects
            self.player.update(self.delta_time, self.objects, None)

            # Render (todo: move into separate Render class?)
            self.screen.fill((0, 0, 0))

            for object in self.objects:
                object.render(self.screen)
            self.player.render(self.screen)

            # Splat to screen
            pygame.display.flip()

game = Game()
