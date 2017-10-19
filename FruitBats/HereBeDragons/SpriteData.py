# REQUIRES UPDATES TO CHECK MOVE AND MODELS
import pygame
import time
import math


class Character:  # The parent class of all sprites
    SPRITE = pygame.Surface((100,100))
    health = 0
    damage = 0
    armour = 0
    location = (0.0, 0.0)


    def __init__(self, InImage, InLocation, InHealth=100, InDamage=10, InArmour=2):
        self.health = InHealth
        self.damage = InDamage
        self.armour = InArmour
        self.img = InImage
        self.location = InLocation

    def is_dead(self):
        if self.health <= 0:
            return True

    def move(self, move_x, move_y):
        """Performs collision checking and moves object by offset of move_x and move_y if possible"""
        self.location = (move_x+self.location[0], move_y+self.location[1])

    def distance(self,a,b):
        """Returns the distance between two points, in tile units"""
        return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))


class PlayerClass(Character):  # The player class

    MAX_SPEED = 200.0  # The maximum running speed, in tiles/sec
    ACCELERATION = 100.0  # Rate of ACCELERATION while running, in tiles/sec/sec
    FRICTION = 400.0  # Rate of slowdown when releasing movement keys
    X_VELOCITY = 0.0  # Rate of movement per axis in tiles/sec
    Y_VELOCITY = 0.0

    def __init__(self, InLocation, InHealth=100, InDamage=10, InArmour=2):
        self.SPRITE = "ImageFiles/temp_player.jpg"
        """Init: Loads default player sprite and scales it up"""
        # Load character image
        self.health = InHealth
        self.damage = InDamage
        self.armour = InArmour
        self.location = InLocation
        self.SPRITE = pygame.image.load(self.SPRITE)
        #self.SPRITE = self.SPRITE.convert(24)

    def update_move(self,delta_time):  # Moves Player, requires delta-time
        # Perform character movement
        key_pressed = pygame.key.get_pressed()

        # Make a normalised vector of movement based on user input
        move_x = 0.0
        move_y = 0.0
        if key_pressed[pygame.K_w]:
            move_y -= 1.0
        if key_pressed[pygame.K_s]:
            move_y += 1.0
        if key_pressed[pygame.K_d]:
            move_x += 1.0
        if key_pressed[pygame.K_a]:
            move_x -= 1.0

        vec_length = self.distance((0, 0), (move_x, move_y))

        if vec_length > 0.000:  # todo: determine why 'if vec_length is not 0.0' didn't work correctly
            # Normalise
            move_x /= vec_length
            move_y /= vec_length

            # Accelerate according to the direction of the vector
            self.X_VELOCITY += move_x * self.ACCELERATION * delta_time
            self.Y_VELOCITY += move_y * self.ACCELERATION * delta_time

            # Cap player max speed
            current_speed = self.distance((0, 0), (self.X_VELOCITY, self.Y_VELOCITY))
            if current_speed > self.MAX_SPEED:
                self.X_VELOCITY *= self.MAX_SPEED / current_speed
                self.Y_VELOCITY *= self.MAX_SPEED / current_speed
        else:
            # Normalise to FRICTION speed at max
            current_speed = self.distance((0, 0), (self.X_VELOCITY, self.Y_VELOCITY))  # player's current speed
            new_length = self.FRICTION  # desired length of the FRICTION slowdown vector

            # If the player is moving slower than the FRICTION rate,
            # cut the FRICTION rate down to cancel out movement entirely
            if current_speed < new_length * delta_time:
                new_length = current_speed / delta_time

            if current_speed > 0:
                move_x = -self.X_VELOCITY * new_length / current_speed
                move_y = -self.Y_VELOCITY * new_length / current_speed

            # Decelerate accordingly
            self.X_VELOCITY += move_x * delta_time
            self.Y_VELOCITY += move_y * delta_time

        # Move player by velocity
        self.move(self.X_VELOCITY * delta_time, self.Y_VELOCITY * delta_time)


class EnemyClass(Character):
    def move(self,move_space):  # Enemy Move - Returns True and moves enemy, else returns False
        if self.check_move(move_space):
            self.location+=move_space
            return True
        return False
