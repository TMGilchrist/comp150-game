import pygame
import pickle

from sprite import Sprite
from button import Button
from get_images import GetImages


class CharacterCreation:

    # Window needs to close when save button is pressed! Trying to change components after saving will throw error.
    # Serialize and deserialize methods should be in another module - possibly in Sprite class. Call with Sprite.serialize.
    # Button in create_buttons shouldn't be properties - *I think*
    # Update class docstring

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

    loading = False
    # loading = True

    def __init__(self, size, hair_list, body_list, legs_list):

        """
        Constructor method.

        Args:
            size (tuple): The size in pixels of the character creation window.
            hair_list (list of images): The images that can be chosen for the character's head.
            body_list (list of images): The images that can be chosen for the character's body.
            legs_list (list of images): The images that can be chosen for the character's legs.
        """

        self.size = size
        self.hair_choices = hair_list
        self.body_choices = body_list
        self.legs_choices = legs_list

        self.body_choices_length = len(self.body_choices)
        self.hair_choices_length = len(self.hair_choices)
        self.legs_choices_length = len(self.legs_choices)

        self.read_component_index("char_creation_index.txt")

        if self.loading:
            self.player_char = self.load_serialized_sprite("player_sprite")

        else:
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

        # Create and draw a new sprite with a base image and the last used components
        blank_sprite = Sprite((128, 128), self.background_colour, pygame.transform.scale(self.blank_base, (128, 128)), self.legs_choices[self.legs_index],
                                                                  self.body_choices[self.body_index], self.hair_choices[self.hair_index], self.blank_component, 0)
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

        # Whole section could probably be neater. Prehaps make ScrollButton and object that inherits from Button with inital size, colour, function etc?
        # Probably don't need to make each button an attribute as buttons can be accessed through buttons list.

        # Create new buttons
        center = (self.size[0] / 2), (self.size[1] / 2)
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

        # Save/finish button
        button_save = Button((100, 50), (center[0] - 50, center[1] + 200), (0, 0, 255), self.main_screen, self.serialize_sprite, ["player_sprite", self.player_char], "foo")

        # Add new buttons to the list of buttons
        self.buttons.append(self.button_hair)
        self.buttons.append(self.button_hair_back)

        self.buttons.append(self.button_body)
        self.buttons.append(self.button_body_back)

        self.buttons.append(self.button_legs)
        self.buttons.append(self.button_legs_back)

        self.buttons.append(button_save)

    def save_component_index(self, save_file):

        """Creates or overwrites the save file, updating the index position when the player saved their sprite."""

        with open(save_file, "w") as f:
            f.write("hair_index " + str(self.hair_index) + "\n")
            f.write("body_index " + str(self.body_index) + "\n")
            f.write("legs_index " + str(self.legs_index) + "\n")
            f.close()

    def read_component_index(self, save_file):

        """Reads the save file and sets the appropriate index value to the saved values."""

        with open(save_file) as f:
            for line in f:
                (key, val) = line.split()
                setattr(self, key, int(val))

    def serialize_sprite(self, file, to_pickle):

        """
        Serialize (pickle) a Sprite instance. Because pygame Surfaces cannot be pickled,
        each surface is converted to a string prior to pickling.

        Args:
              file (string): The name of the binary file where the serialized Sprite will be stored.
              to_pickle (Sprite instance): The instance of Sprite to be pickled.
        """

        print("Sprite serialized")

        binary_file = open(file + ".bin", mode="wb")

        to_pickle.image = pygame.image.tostring(to_pickle.image, "RGBA")
        to_pickle.base = pygame.image.tostring(to_pickle.base, "RGBA")
        to_pickle.legs = pygame.image.tostring(to_pickle.legs, "RGBA")
        to_pickle.body = pygame.image.tostring(to_pickle.body, "RGBA")
        to_pickle.hair = pygame.image.tostring(to_pickle.hair, "RGBA")
        to_pickle.feet = pygame.image.tostring(to_pickle.feet, "RGBA")

        to_pickle.sprite_base = pygame.image.tostring(to_pickle.sprite_base, "RGBA")

        pickle.dump(to_pickle, binary_file)
        binary_file.close()

    def load_serialized_sprite(self, file):

        """
        Deserialize (unpickle) a Sprite instance. As the Surfaces are pickled as strings, they must be converted back to
        Surfaces after unpickling.

        Args:
             file (string): The name of the binary file from which to retrieve the serialized Sprite.

        Returns:
            loaded_sprite (Sprite): The instance of Sprite that was pickled.
        """

        binary_file = open(file + ".bin", mode="rb")
        loaded_sprite = pickle.load(binary_file)
        binary_file.close()

        loaded_sprite.image = pygame.image.fromstring(loaded_sprite.image, loaded_sprite.size, "RGBA")
        loaded_sprite.base = pygame.image.fromstring(loaded_sprite.base, loaded_sprite.size, "RGBA")
        loaded_sprite.legs = pygame.image.fromstring(loaded_sprite.legs, loaded_sprite.size, "RGBA")
        loaded_sprite.body = pygame.image.fromstring(loaded_sprite.body, loaded_sprite.size, "RGBA")
        loaded_sprite.hair = pygame.image.fromstring(loaded_sprite.hair, loaded_sprite.size, "RGBA")
        loaded_sprite.feet = pygame.image.fromstring(loaded_sprite.feet, (16, 16), "RGBA")            # No component set for feet therefore size has not been scaled up

        loaded_sprite.sprite_base = pygame.image.fromstring(loaded_sprite.sprite_base, loaded_sprite.size, "RGBA")

        return loaded_sprite


# Calling as test
images = GetImages("../Assets", ".png", (128, 128))

test_window = CharacterCreation((800, 600), images.hair, images.body, images.legs)
test_window.draw_win()

test_window.save_component_index("char_creation_index.txt")

