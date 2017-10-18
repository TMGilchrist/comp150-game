import pygame

class CharacterClass:
    def character_movements(self):





# Parameters
g_width = 640
g_height = 480

# Init Python
pygame.init()
screen = pygame.display.set_mode((g_width, g_height))

# Load character image
character = pygame.image.load('graphics/game_character.png')
character = character.convert(24)

# Image scale
character = pygame.transform.scale(character, (character.get_width() * 4, character.get_height() * 4))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and
                 event.key == pygame.K_ESCAPE):
            running = False
    screen.blit(character, (0, 0))
    pygame.display.flip()
