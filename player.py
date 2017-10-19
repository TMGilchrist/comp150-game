# Standard imports
import time
import math
import random

# Third party imports
import pygame

# Local imports (todo: remove these comments when we're all comfortable with
#                this ordering)


def distance((x1, y1), (x2, y2)):
    """Returns the distance between two points, in tile units"""
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


class CollisionParams:
    shape = 0  # Todo: Add sphere collision etc?
    x = 0  # X offset of collision box in tiles (relative to parent object)
    y = 0  # Y offset of collision box in tiles
    width = 0  # Width of collision box in tiles
    height = 0  # Height of collision box in tiles
    solid = False


class ObjectClass:
    # Main variables for characters
    x = 0  # in game tile units (1.0 = 1 tile)
    y = 0  # in game tile units
    sprite = None  # current object sprite (todo: animations etc)
    collision = CollisionParams()  # collision data

    def __init__(self, x, y):
        """Initialise object at the given position"""
        self.x = x
        self.y = y

    def move(self, move_x, move_y):
        """Performs collision checking and moves object by offset of move_x and move_y if possible"""
        # Decide where the object is (trying) to go
        desired_x = self.x + move_x
        desired_y = self.y + move_y
        # Perform collision detection with objects
        if self.collision.solid:
            # Determine current area of our collision box
            box_left = self.x + self.collision.x
            box_top = self.y + self.collision.y
            box_right = box_left + self.collision.width
            box_bottom = box_top + self.collision.height
            # Check with other objects
            for object in objects:
                obj_box_left = object.x + object.collision.x
                obj_box_top = object.y + object.collision.y
                obj_box_right = obj_box_left + object.collision.width
                obj_box_bottom = obj_box_top + object.collision.height

        self.x = desired_x
        self.y = desired_y

    def render(self):
        """Renders the object sprite at its given position (overloadable function)"""
        if self.sprite is not None:
            screen.blit(self.sprite,
                        (self.x * TILE_WIDTH, self.y * TILE_HEIGHT))


class CharacterClass(ObjectClass):
    etc = 0  # Todo


class PlayerClass(CharacterClass):
    max_speed = 10.0  # The maximum running speed, in tiles/sec
    acceleration = 30.0  # Rate of acceleration while running, in tiles/sec/sec
    friction = 70.0  # Rate of slowdown when releasing movement keys
    x_velocity = 0.0  # Rate of movement per axis in tiles/sec
    y_velocity = 0.0

    def __init__(self, x, y):
        """Init: Loads default player sprite and scales it up"""
        # Load character image
        self.sprite = pygame.image.load('graphics/game_character.png')
        self.sprite = self.sprite.convert(24)
        # Scale character so we can see his beauty
        self.sprite = pygame.transform.smoothscale(
                        self.sprite,
                        (TILE_WIDTH, TILE_HEIGHT))
        self.x = x
        self.y = y
        self.collision.width = 1.0
        self.collision.height = 1.0
        self.collision.solid = True

    def update(self):
        global delta_time
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

        vec_length = distance((0, 0), (move_x, move_y))
        if vec_length > 0.000:  # todo: determine why 'if vec_length is not 0.0' didn't work correctly
            # Normalise
            move_x /= vec_length
            move_y /= vec_length

            # Accelerate according to the direction of the vector
            self.x_velocity += move_x * self.acceleration * delta_time
            self.y_velocity += move_y * self.acceleration * delta_time

            # Cap player max speed
            current_speed = distance((0, 0), (self.x_velocity, self.y_velocity))
            if current_speed > self.max_speed:
                self.x_velocity *= self.max_speed / current_speed
                self.y_velocity *= self.max_speed / current_speed
        else:
            # Normalise to friction speed at max
            current_speed = distance((0, 0), (self.x_velocity, self.y_velocity))  # player's current speed
            new_length = self.friction  # desired length of the friction slowdown vector

            # If the player is moving slower than the friction rate,
            # cut the friction rate down to cancel out movement entirely
            if current_speed < new_length * delta_time:
                new_length = current_speed / delta_time

            if current_speed > 0:
                move_x = -self.x_velocity * new_length / current_speed
                move_y = -self.y_velocity * new_length / current_speed

            # Decelerate accordingly
            self.x_velocity += move_x * delta_time
            self.y_velocity += move_y * delta_time

        # Move player by velocity
        self.move(self.x_velocity * delta_time, self.y_velocity * delta_time)


class PikachuStatue(ObjectClass):
    def __init__(self, x, y):
        self.sprite = pygame.image.load('graphics/pikachu.png')
        self.sprite = pygame.transform.smoothscale(self.sprite, (TILE_WIDTH, TILE_HEIGHT))
        self.sprite = self.sprite.convert(24)
        self.x = x
        self.y = y
        self.collision.width = 1.0
        self.collision.height = 1.0
        self.collision.solid = True


# Constants
TILE_WIDTH = 40  # temporary--plug in map defaults later!
TILE_HEIGHT = 40  # ditto

# Parameters
g_width = 640
g_height = 480

# Init Python
pygame.init()
screen = pygame.display.set_mode((g_width, g_height))

# Init character
player = PlayerClass(0, 0)

# Init Objects
objects = list()
for i in xrange(10):
    objects.append(PikachuStatue(random.randint(0, 10), random.randint(0, 10)))

# Init main game parameters (todo: split all this into a class, no globals)
tick_time = time.clock()  # time at the beginning of the current game tick
delta_time = 0.0

# Main loop
running = True
while running:
    # Update timing
    last_time = tick_time
    tick_time = time.clock()

    delta_time = tick_time - last_time

    # Perform PyGame event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and
                 event.key == pygame.K_ESCAPE):
            running = False

    player.update()

    # Perform rendering (todo: move into separate Render class)
    screen.fill((0, 0, 0))

    for objects in objects:
        objects.render()
    player.render()
    pygame.display.flip()
