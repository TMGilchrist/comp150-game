import pygame
from HereBeDragons import Const

# REQUIRES UPDATES


class CastleClass():
    DATA_WHEN_UPGRADED = {}  # Update with models
    img = pygame.Surface((100,100))  # update with block size
    lvl = 0
    Kingdoms = [[0 for x in range (Const.MAP.SIZE_X_MAX)]for y in range (Const.MAP.SIZE_X_MAX)]  # SIZE OF MAP
    location = (0,0)

    def inc_kingdom_size(self):
        print

    def __init__(self,InLocation):
        self.location = InLocation

    def upgrade(self):  # returns true if upgraded, returns false if max level
        if len(self.DATA_WHEN_UPGRADED) >= self.lvl:
            return False
        self.lvl += 1
        self.img = self.DATA_WHEN_UPGRADED[self.lvl]
        return True

