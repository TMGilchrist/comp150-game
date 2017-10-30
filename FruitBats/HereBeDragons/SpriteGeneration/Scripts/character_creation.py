import sys
sys.path.append("//tremictssan.fal.ac.uk\userdata\TG190896\My Documents\Py2.7\HereBeDragons\Utility")
import pygame

from sprite import Sprite
from button import Button
import glob


class CharacterCreation:

    # Need to add a function to save the sprite.

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

    main_screen = None
    background_colour = (222, 184, 135)
    buttons = []

    char_position = (326, 236)

    player_char = None

    body_choices = []
    hair_choices = []
    legs_choices = []

    body_index = -1
    hair_index = -1
    legs_index = -1

    body_choices_length = 0
    hair_choices_length = 0
    legs_choices_length = 0

    # These should be put into a list
    # button_body = None
    # button_body_back = None

    # Constructor instantiates a sprite with a blank base
    def __init__(self, size, hair_list, body_list, legs_list):

        """
        Constructor method.

        Args:
            size (tuple): The size in pixels of the character creation window.
            hair_list (list of images): The images that can be chosen for the character's head.
            body_list (list of images): The images that can be chosen for the character's body.
        """

        self.size = size
        self.hair_choices = hair_list
        self.body_choices = body_list
        self.legs_choices = legs_list

        self.body_choices_length = len(self.body_choices)
        self.hair_choices_length = len(self.hair_choices)
        self.legs_choices_length = len(self.legs_choices)

        self.player_char = self.load_blank_sprite()

    def draw_win(self):

        """Main method for the class. This creates the character creation window and checks for player input."""

        print("Drawing screen for first time")
        self.main_screen = pygame.display.set_mode(self.size)
        self.main_screen.fill(self.background_colour)

        self.create_buttons()

        self.update_screen()

        # Keep window open until user closes it
        done = False

        while not done:
            for event in pygame.event.get():

                # Each button checks if it was clicked
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        button.check_click(pygame.mouse.get_pos())

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True

    def update_screen(self):

        """Updates the character creation screen. Blits the character sprite to the screen and updates it."""

        # Update Screen
        self.main_screen.blit(self.player_char.image, self.char_position)
        pygame.display.flip()

        print("Screen updated")

    def load_blank_sprite(self):

        """
        Instantiates a new Sprite with a blank base and blank components as placeholders and draws the sprite image.

        Returns:
            blank_sprite (Sprite): A Sprite with base image and blank components.
        """

        # Create and draw a new sprite with a base image and blank components
        blank_sprite = Sprite((128, 128), self.background_colour, pygame.transform.scale(self.blank_base, (128, 128)), self.blank_component, self.blank_component, self.blank_component, self.blank_component, 0)
        blank_sprite.draw()

        return blank_sprite

    def scroll_components(self, component, direction):

        """
        Scrolls in a direction (backwards or forwards) through a list of component images and updates the player's sprite

        Args:
            component (string): The component to change when the player gives input (presses a 'button')
            direction (int): 1 = scrolling forward in list, -1 = scrolling backwards in list.
        """

        # Get the index of the relevant component list
        index = getattr(self, component + "_index")
        list_length = getattr(self, component + "_choices_length")

        # Move through list
        if direction == 1:
            index += 1

        elif direction == -1:
            index -= 1

        # If index exceeds list bounds, reset to 0
        if (index >= list_length) or (index <= -list_length):
            print("Index at max! " + str(list_length))
            index = 0
        else:
            print("Index = " + str(index))

        # Update the index of the relevant component
        setattr(self, component + "_index", index)

        # Update component of sprite with image from location in list
        self.player_char.update([component], [getattr(self, component + "_choices")[index]])
        self.update_screen()

    def create_buttons(self):

        """
        Instantiates all the buttons needed for the character creation window.
        The buttons are positioned based on the positioning of the player character.
        Each button is also appended to the list of buttons.
        """

        # Create new buttons

        right = (self.char_position[0] + 150)
        left = (self.char_position[0] - 100)
        y = self.char_position[1]

        # Hair options
        self.button_hair = Button((50, 50), (right, y - 100), (0, 255, 0), self.main_screen, self.scroll_components, ["hair", 1], "foo")
        self.button_hair_back = Button((50, 50), (left, y - 100), (255, 0, 0), self.main_screen, self.scroll_components, ["hair", -1], "foo")

        # Body options
        self.button_body = Button((50, 50), (right, y), (0, 255, 0), self.main_screen, self.scroll_components, ["body", 1], "foo")
        self.button_body_back = Button((50, 50), (left, y), (255, 0, 0), self.main_screen, self.scroll_components, ["body", -1], "foo")

        # Leg options
        self.button_legs = Button((50, 50), (right, y + 100), (0, 255, 0), self.main_screen, self.scroll_components, ["legs", 1], "foo")
        self.button_legs_back = Button((50, 50), (left, y + 100), (255, 0, 0), self.main_screen, self.scroll_components, ["legs", -1], "foo")

        # Add new buttons to the list of buttons
        self.buttons.append(self.button_hair)
        self.buttons.append(self.button_hair_back)

        self.buttons.append(self.button_body)
        self.buttons.append(self.button_body_back)

        self.buttons.append(self.button_legs)
        self.buttons.append(self.button_legs_back)


# Calling as test
bodies = []
hair = []
legs = []

for filename in glob.glob("../Assets/Sprites/body/*.png"):
    bodies.append(pygame.transform.scale(pygame.image.load(filename), (128, 128)))

for filename in glob.glob("../Assets/Sprites/hair/*.png"):
    hair.append(pygame.transform.scale(pygame.image.load(filename), (128, 128)))

for filename in glob.glob("../Assets/Sprites/legs/*.png"):
    legs.append(pygame.transform.scale(pygame.image.load(filename), (128, 128)))

test_window = CharacterCreation((800, 600), hair, bodies, legs)
test_window.draw_win()




