import sys, os
sys.path.append("//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Utility")
import pygame

from sprite import Sprite
from button import Button
import glob


class CharacterCreation:

    """
    CharacterCreation class. This class displays a character creation window and allows the user to edit the apperance
    of their character.

    Attributes:
        path_to_assets (string): The file path to the assets folder. This should later be added to the constructor so it
                                 can be passed in when the class is instantiated.
        blank_component (image): A blank image that is used as a placeholder
        blank_base (image): The image used for the base of the sprite
        main_screen (pygame.Display): The character creation window
        player_char (Sprite): The player character's Sprite. player_char.image used to access the image
        body_choices (list of images): The images that the player can choose from for the body component.
    """

    path_to_assets = "../Assets"
    blank_component = pygame.image.load(path_to_assets + "/Sprites/blankComponent.png")
    blank_base = pygame.image.load(path_to_assets + "/Sprites/base/base1.png")

    main_screen = 0

    player_char = 0

    body_choices = []

    index = -1

    # These should be put into a list
    button_body = None
    button_body_back = None

    # Constructor instantiates a sprite with a blank base
    def __init__(self, size, head_list, body_list):

        """
        Constructor method.

        Args:
            size (tuple): The size in pixels of the character creation window.
            head_list (list of images): The images that can be chosen for the character's head.
            body_list (list of images): The images that can be chosen for the character's body.
        """

        self.size = size
        # self.head_list = head_list
        self.body_choices = body_list
        self.player_char = self.load_blank_sprite()

    # Draw the character creation window
    def draw_win(self):

        """Main method for the class. This creates the character creation window and checks for player input."""

        print("Drawing screen for first time")
        self.main_screen = pygame.display.set_mode(self.size)
        self.main_screen.fill((222, 184, 135))

        self.button_body = Button((100, 100), (0, 0), (0, 255, 0), self.main_screen, self.scroll_components, [self, "body"], "foo")
        # self.button_body_back = Button((100, 100), (0, 100), (255, 0, 0), self.main_screen, self.test_use, [] "foo")

        self.update_screen()
        # self.scroll_components("body")

        # Keep window open until user closes it
        done = False

        while not done:
            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.button_body.check_click(pygame.mouse.get_pos())        # Buttons should be added to a list and event checker iterates through list
                    # self.button_body_back.check_click(pygame.mouse.get_pos())

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

    def update_screen(self):

        """Updates the character creation screen. Blits the character sprite to the screen and updates it."""

        # Update Screen
        self.main_screen.blit(self.player_char.image, (400, 300))
        pygame.display.flip()

        print("Screen updated")

    # Method returns a sprite base
    def load_blank_sprite(self):

        """
        Instantiates a new Sprite with a blank base and blank components as placeholders and draws the sprite image.

        Returns:
            blank_sprite (Sprite): A Sprite with base image and blank components.
        """

        # Create and draw a new sprite with a base image and blank components
        blank_sprite = Sprite((64, 64), pygame.transform.scale(self.blank_base, (64, 64)), self.blank_component, self.blank_component, self.blank_component, self.blank_component, 0)
        blank_sprite.draw()

        return blank_sprite

    # argument "direction" should be added, to specify if index is incremented or decremented
    def scroll_components(self, component):

        """
        Scrolls in a direction (back or forwards) through a list of component images and updates the player's sprite

        Args:
            component (string): The component to change when the player gives input (presses a 'button')

        """

        self.index += 1

        # Update component of sprite with image from location in list
        self.player_char.update([component], [getattr(self, component + "_choices")[self.index]])
        self.update_screen()

    def scroll_components_test(self, component):

        """
        Method to check for user input. This is a placeholder method to replicate the functionality of buttons.
        Inputting 1 will scroll forward though the list of component images and -1 will scroll backwards. Any other input
        will exit the function.

        Args:
            component (string): The component to change when the player gives input (presses a 'button')

        """

        print("Scroll components running")
        fake_button = 1
        index = -1

        while True:
            for event in pygame.event.get():
                pass  # clear the event loop by doing nothing

            fake_button = int(raw_input("Input 1 for scroll forwards, -1 for scroll back"))

            if fake_button == 1:
                index += 1

            elif fake_button == -1:
                index -= 1

            else:
                break

            print("index = " + str(index))
            print("Updating sprite")

            # Update component of sprite with image from location in list
            self.player_char.update([component], [getattr(self, component + "_choices")[index]])
            self.update_screen()




# Calling as test
bodies = []

for filename in glob.glob("../Assets/Sprites/body/*.png"):
    bodies.append(pygame.transform.scale(pygame.image.load(filename), (64, 64)))

test_window = CharacterCreation((800, 600), 0, bodies)
test_window.draw_win()

# test_window.scroll_components("body")





