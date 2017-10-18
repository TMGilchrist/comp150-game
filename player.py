# Standard imports
import time

# Third party imports
import pygame

# Local imports (todo: remove these comments when we're all comfortable with
#                this ordering)


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
    def __init__(self, x, y):
        """Init: Loads default player sprite and scales it up"""
        # Load character image
        self.sprite = pygame.image.load('graphics/game_character.png')
        self.sprite = self.sprite.convert(24)
        # Scale character so we can see his beauty
        self.sprite = pygame.transform.scale(
                        self.sprite,
                        (self.sprite.get_width() * 4,
                         self.sprite.get_height() * 4))

    def update(self):
        # Character movement in response to input will go here :)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.y -= 1 * delta_time
        if key_pressed[pygame.K_s]:
            self.y += 1 * delta_time
        if key_pressed[pygame.K_d]:
            self.x += 1 * delta_time
        if key_pressed[pygame.K_a]:
            self.x -= 1 * delta_time


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
