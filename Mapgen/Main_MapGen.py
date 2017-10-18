import pygame
import random


class MAPCONST:
    BLOCK_SIZE = 80
    SIZE_Y_MAX = 30
    SIZE_X_MAX = 30
    TILE_INFO = [ #INFORMATION ON TILES (SPAWN WEIGHT, FILE NAME)
        [40,"TEMP1.jpg"],
        [3,"TEMP2.jpg"]
    ]

class MapClass:
    Map = [[0 for x in range (MAPCONST.SIZE_X_MAX)]for y in range (MAPCONST.SIZE_X_MAX)]
    def __init__(self,Seed=0):
        if (not (Seed == 0)):
            random.seed(Seed)
        total_weight=0
        for i in MAPCONST.TILE_INFO:
            total_weight += i[0]
        for y in range(0,MAPCONST.SIZE_Y_MAX):
            for x in range(0,MAPCONST.SIZE_Y_MAX):
                for i in range(0,len(MAPCONST.TILE_INFO)):
                    if random.randint(0, total_weight)//MAPCONST.TILE_INFO[i][0]<= 1:
                        self.Map[x][y] = i

    def render(self):
        ret = pygame.Surface((MAPCONST.SIZE_X_MAX*MAPCONST.BLOCK_SIZE,MAPCONST.SIZE_Y_MAX*MAPCONST.BLOCK_SIZE))
        for y in range(0,MAPCONST.SIZE_Y_MAX):
            for x in range(0, MAPCONST.SIZE_X_MAX):
                temp_img = pygame.image.load(MAPCONST.TILE_INFO[self.Map[x][y]][1]).convert()
                ret.blit(temp_img,(x*MAPCONST.BLOCK_SIZE,y*MAPCONST.BLOCK_SIZE))
        return ret

Map= MapClass()
screen = pygame.display.set_mode((800,500))
pygame.init()

img=Map.render()


def SCREEN():
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done=True
        screen.blit(img,(0,0))
        pygame.display.flip()
SCREEN()