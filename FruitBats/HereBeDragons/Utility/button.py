import pygame


class Button:

    button = None
    button_bounds = None
    parent_surface = None

    def __init__(self, size, message, parent_surface, position):

        """
        Constructor method. Draws a button on a surface.

        Args:
            size (tuple): Size of the button.
            message (string): Message to display on the button.
            parent_surface (pygame.Surface): The surface on which to draw the button.
            position (tuple): The position at which to draw the button.
        """

        self.size = size
        self.message = message
        self.parent_surface = parent_surface
        self.position = position

        self.button = pygame.Surface(self.size)
        self.button_bounds = self.button.get_rect()
        self.draw()

    def on_click(self):
        print("clicked")

    def check_click(self, mouse_position):
        print("Click being checked")

        if self.button_bounds.collidepoint(mouse_position) == True:
            self.on_click()

    def draw(self):
        self.button.fill((255, 0, 0))
        self.parent_surface.blit(self.button, self.position)


main_screen = pygame.display.set_mode((800, 600))
main_screen.fill((222, 184, 135))

test_button = Button((100, 100), "foo", main_screen, (0, 0))

pygame.display.flip()

# Keep window open until user closes it
done = False

while not done:
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            test_button.check_click(pygame.mouse.get_pos())

        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True