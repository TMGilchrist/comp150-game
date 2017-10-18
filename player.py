# Standard imports
import time
import math

# Third party imports
import pygame

# Local imports (todo: remove these comments when we're all comfortable with
#                this ordering)


def distance((x1, y1), (x2, y2)):
    """Returns the distance between two points, in tile units"""
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


class ObjectClass:
    # Main variables for characters
    x = 0  # position is in game tiles
    y = 0
    sprite = None

    def __init__(self, x, y):
        """Initialise object at the given position"""
        self.x = x
        self.y = y


    def move(self, move_x, move_y):
        """Performs collision checking and moves object by offset of move_x and move_y if possible"""
        self.x += move_x
        self.y += move_y
        # Todo: collision detection

    def render(self):
        """Renders the object sprite at its given position (overloadable function)"""
        if self.sprite is not None:
            screen.blit(self.sprite,
                        (self.x * TILE_WIDTH, self.y * TILE_HEIGHT))


class CharacterClass(ObjectClass):
    etc = 0  # Todo


class PlayerClass(CharacterClass):
    max_speed = 6.0  # The maximum running speed, in tiles/sec
    acceleration = 10.0  # Rate of acceleration while running, in tiles/sec/sec
    friction = 30.0  # Rate of slowdown when releasing movement keys
    x_velocity = 0.0  # Rate of movement per axis in tiles/sec
    y_velocity = 0.0

    def __init__(self, x, y):
        """Init: Loads default player sprite and scales it up"""
        # Load character image
        self.sprite = pygame.image.load('graphics/game_character.png')
        self.sprite = self.sprite.convert(24)
        # Scale character so we can see his beauty
        self.sprite = pygame.transform.scale(
                        self.sprite,
                        (self.sprite.get_width() * 3,
                         self.sprite.get_height() * 3))
        self.x = x
        self.y = y

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

        if move_x is not 0.0 or move_y is not 0.0:
            # Normalise
            vec_length = distance((0, 0), (move_x, move_y))
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
            new_length = self.friction # desired length of the friction slowdown vector

            # If the player is moving slower than the friction rate,
            # cut the friction rate down to cancel out movement entirely
            if current_speed < new_length:
                new_length = current_speed

            if current_speed > 0:
                move_x = -self.x_velocity * new_length / current_speed
                move_y = -self.y_velocity * new_length / current_speed

            # Decelerate accordingly
            self.x_velocity += move_x * delta_time
            self.y_velocity += move_y * delta_time

        # Move player by velocity
        self.move(self.x_velocity * delta_time, self.y_velocity * delta_time)


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
    player.render()
    pygame.display.flip()
