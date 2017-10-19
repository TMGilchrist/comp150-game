import pygame
import time
import os
print os.getcwd()

from HereBeDragons import Const, MapGen, SpriteData

pygame.init()
screen = pygame.display.set_mode((800,500))

#INITIALISE HERE


Player = SpriteData.PlayerClass((0,0))
MapGen.Map.render()


def Update(delta_time):
    Player.update_move(delta_time)
    screen.blit(MapGen.Map.img,(-Player.location[0],-Player.location[1]))
    screen.blit(Player.SPRITE,(400,250))





tick_time = time.clock()
delta_time = 0.0
running = True
while running:
    last_time = tick_time
    tick_time = time.clock()
    delta_time = tick_time - last_time
    # Perform PyGame event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and
                 event.key == pygame.K_ESCAPE):
            running = False
    Update(delta_time)
    pygame.display.flip()