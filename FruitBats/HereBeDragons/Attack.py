import pygame
import cmath
import math

from Objects import Object
from Collision import CollisionParams
from Map import MapClass


class Swipe(Object):  # todo: load swipe animation
    original_sprite = None

    def __init__(self, x, y):
        self.original_sprite = pygame.image.load("graphics/sword.png")
        self.sprite = self.original_sprite
        self.x = x
        self.y = y
        self.collision = CollisionParams((0, 0), (32, 32), False)

    def update(self, delta_time, player, object_list, map):
        mouse_x = float(pygame.mouse.get_pos()[0]) / MapClass.TILE_SIZE
        mouse_y = float(pygame.mouse.get_pos()[1]) / MapClass.TILE_SIZE
        angle = float(math.atan2((self.y - mouse_y), (mouse_x - self.x)))
        self.sprite_angle = float(math.degrees(angle) - 90)

#    def attack(self):
 #       self.attack = False
  #      self.mouse.xy = pygame.mouse.get_pos()
   #     if pygame.mouse.get_pressed()[0]:
    #        self.attack = True