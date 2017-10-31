import pygame


class Sprite:

    """
    Sprite Class. This class contains methods for drawing, updating and saving a sprite as a single image. Needs a render function!

    Attributes:
        image (pygame.Surface): This is the image for the sprite in the form of a surface which can be redrawn if the sprite is updated.
    """

    # The image used for the sprite
    image = None

    def __init__(self, size, background_colour, base, legs, body, hair, feet, weapon):

        """
        Constructor for sprite class.

        Args:
            size (tuple): The size of the sprite in pixels.
            background_colour (colour): The colour, including alpha value, of the background of the sprite image.
            base (pygame.Surface): The image to use for the sprite base.
            legs (pygame.Surface): The image to use for the sprite's legs.
            body (pygame.Surface): The image to use for the sprite's body.
            hair (pygame.Surface): The image to use for the sprite's head.
            feet (pygame.Surface): The image to use for the sprite's feet.
            weapon (pygame.Surface): The image to use for the sprite's weapon. Note that in the current implementation this
                                     is always passed a placeholder of 0, as weapon sprites have not been added to the assets folder.
                                     Similarily, the weapon image is not blitted to the sprite image in the draw functions, as there is no image.
        """

        self.size = size
        self.background_colour = background_colour
        self.base = base
        self.legs = legs
        self.body = body
        self.hair = hair
        self.feet = feet
        self.weapon = weapon

        print("Sprite body is " + str(self.body))

        self.sprite_base = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        #self.sprite_base.set_alpha(255)

    def draw(self):

        """Draws the sprite's component images onto a PyGame surface and assigns it to the image property."""

        # clear surface
        self.sprite_base.fill(self.background_colour)

        self.sprite_base.blit(self.base, (0, 0))
        self.sprite_base.blit(self.legs, (0, 0))
        self.sprite_base.blit(self.body, (0, 0))
        self.sprite_base.blit(self.hair, (0, 0))
        self.sprite_base.blit(self.feet, (0, 0))

        self.image = self.sprite_base

    def draw_with_position(self, base_pos, body_pos, legs_pos, head_pos):

        """
        Draws the sprite's component images onto a PyGame surface at
        specified positions and assigns the surface to the image property.

        Args:
            base_pos (tuple): Position of the base image.
            body_pos (tuple): Position of the body image.
            legs_pos (tuple): Position of the legs image.
            head_pos (tuple): Position of the head image.
        """

        self.sprite_base.blit(self.base, base_pos)
        self.sprite_base.blit(self.legs, legs_pos)
        self.sprite_base.blit(self.body, body_pos)
        self.sprite_base.blit(self.hair, head_pos)
        self.sprite_base.blit(self.feet, (0, 0))

        # Save sprite
        self.image = self.sprite_base

    def update(self, to_update, new_values):

        """
        Updates the sprite image. Can be called with multiple values to change at once.

        Args:
            to_update (list of strings): The components to change, referencing the sprite properties.
            new_values (list of images): The new images for the components being changed .
        """

        for i in range (0, len(to_update)):
            setattr(self, to_update[i], new_values[i])

        self.draw()

    def save_with_id(self, save_path, file_type):

        """
        Saves the sprite image to file with a unique name and records the name used in a text document.
        Whenever a sprite is saved the text document is checked to ensure that the same name is not used twice.
        If the document does not exist, one will be created.

        Args:
              save_path (string): The file path in which to save the image.
              file_type (string): The file extension to use when saving the image.
        """

        sprite_id = 0

        with open("spriteNames.txt", "a+") as f:
            for line in f:
                sprite_id += 1

            f.write("sprite" + str(sprite_id) + "\n")
            f.close()

        pygame.image.save(self.image, save_path + "/sprite" + str(sprite_id) + "." + file_type)
