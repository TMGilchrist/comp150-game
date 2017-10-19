import pygame
import random
from HereBeDragons import Const


class MapClass:
    Map = [[0 for x in range(0,Const.MAP.SIZE_X)]for y in range(0,Const.MAP.SIZE_X)]
    img = pygame.Surface((Const.MAP.SIZE_X,Const.MAP.SIZE_Y))
    def __init__(self, seed=0):
        if not (seed == 0):
            random.seed(seed)
        total_weight=0
        for i in Const.MAP.TILE_INFO:
            total_weight += i[0]
        for y in range(0, Const.MAP.SIZE_Y):
            for x in range(0, Const.MAP.SIZE_X):
                rand = random.randint(0, total_weight)
                ndone = True
                for i in range(0,len(Const.MAP.TILE_INFO)):  #Turns random number into Map tile
                    rand -= Const.MAP.TILE_INFO[i][0]
                    if rand <= 0 and ndone:
                        ndone = False
                        self.Map[x][y] = i

    def render(self):
        ret = pygame.Surface((Const.MAP.SIZE_X*Const.MAP.BLOCK_SIZE,Const.MAP.SIZE_Y*Const.MAP.BLOCK_SIZE))
        for y in range(0,Const.MAP.SIZE_Y):
            for x in range(0, Const.MAP.SIZE_X):
                temp_img = pygame.image.load(Const.MAP.TILE_INFO[self.Map[x][y]][1]).convert()
                ret.blit(temp_img,(x*Const.MAP.BLOCK_SIZE,y*Const.MAP.BLOCK_SIZE))
        self.img = ret



Map = MapClass()