# import pygame

from Map import MapClass
from Collision import CollisionParams


class Object:
    # Main variables for characters
    x = 0  # in game tile units (1.0 = 1 tile)
    y = 0  # in game tile units
    sprite = None  # current object sprite (todo: animations etc)
    collision = None  # collision data (must be set in initialiser!)

    def __init__(self, x, y):
        """Initialise object at the given position"""
        self.x = x
        self.y = y
        self.collision = CollisionParams((0.0, 0.0), (1.0, 1.0), True)

    def update(self, delta_time, player, object_list, map):
        pass  # to be overloaded by objects

    def render(self, screen):
        """Renders the object (function overloadable by subclasses)"""
        if self.sprite is not None:
            screen.blit(self.sprite,
                        (self.x * MapClass.TILE_SIZE,
                         self.y * MapClass.TILE_SIZE))

    def move(self, (move_x, move_y), object_list):
        """Performs collision checking and moves object by offset of move_x and
           move_y if possible

           (move_x, move_y) -- How far to move, in tile units
           object_list -- List of objects in the environment (for collision)

           Todo: Push the player out of a surface in the opposite direction
           to their attempted movement, return a vector portraying how much
           they moved
        """

        # Decide where the object is (trying) to go
        desired_x = self.x + move_x
        desired_y = self.y + move_y
        collided = False
        # Perform collision detection with objects
        if self.collision.solid:
            # Determine current area of our collision box
            box_left = desired_x + self.collision.x
            box_top = desired_y + self.collision.y
            box_right = box_left + self.collision.width
            box_bottom = box_top + self.collision.height
            # Check with other objects
            for object in object_list:
                if object == self:
                    continue  # don't collide with yourself plz
                obj_box_left = object.x + object.collision.x
                obj_box_top = object.y + object.collision.y
                obj_box_right = obj_box_left + object.collision.width
                obj_box_bottom = obj_box_top + object.collision.height
                if not (box_left >= obj_box_right or
                                box_right <= obj_box_left or
                                box_top >= obj_box_bottom or
                                box_bottom <= obj_box_top):
                    desired_x = self.x
                    desired_y = self.y
                    collided = True

        self.x = desired_x
        self.y = desired_y
        return not collided
