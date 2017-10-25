"""Skeleton file -- not a part of the actual program yet
Up for review: revise as necessary

(Louis and Tomas) These are the objects we created for player movement and
collision detection, etc.
"""

# CollisionParams: defines dimensions, offsets, etc of a collision box
#                  used by objects.
class CollisionParams:
    shape = 0  # Todo: Add sphere collision etc?
    x = 0  # X offset of collision box in tiles (relative to parent object)
    y = 0  # Y offset of collision box in tiles
    width = 0  # Width of collision box in tiles
    height = 0  # Height of collision box in tiles
    solid = False

    def __init__(self, solid, x, y, width, height)
    """init: initialises parameters, simple as"""

# ObjectClass: main base class for objects that move and/or interact
class ObjectClass:
    # Main variables for characters
    x = 0  # in game tile units (1.0 = 1 tile)
    y = 0  # in game tile units
    x_velocity = 0.0  # rate of movement per axis in tiles/sec
    y_velocity = 0.0
    sprite = None  # current object sprite (todo: animations etc)
    collision = CollisionParams()  # collision dimensions, whether solid, etc

    def __init__(self)
    # primary (overloadable) functions
    def update(self, delta_time, object_list, map)
    """update: called once per frame
            delta_time = time passed since last frame in seconds,
            object_list = list of all other objects,
            map = pointer to map class for collision checking, hazards etc
    """
    def render(self, screen)
    """render: called once per frame by GameClass during rendering
            screen = the surface to render to
    """

    # general functions
    def move(self, x, y)
    """move: moves this object by an offset of x and y
       if a collision occurs and this object is solid, the movement is blocked
    """

# CharacterClass: Class used for game characters including players and enemies
# todo individual sprite components?
class CharacterClass(ObjectClass):
    etc = 0  # Todo

# PlayerClass: Includes player movement characteristics, maybe HP, etc?
# todo expand based on battle mechanics, interactions, etc etc
class PlayerClass(CharacterClass):
    max_speed = 7.0  # The maximum running speed, in tiles/sec
    acceleration = 35.0  # Rate of acceleration while running, in tiles/sec/sec
    friction = 90.0  # Rate of slowdown when releasing movement keys