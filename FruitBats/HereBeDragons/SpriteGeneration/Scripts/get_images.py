import pygame
import glob


class GetImages:

    """
    GetImages class. This class is used to load the component images into lists in preperation for generating a random sprite.

    Attributes:
        base (list) = list of images to be used for the sprite base
        legs (list) = list of images to be used for the sprite legs
        body (list) = list of images to be used for the sprite body
        hair (list) = list of images to be used for the sprite hair
        feet (list) = list of images to be used for the sprite feet  
    """

    base = []
    legs = []
    body = []
    hair = []
    feet = []

    def __init__(self, path_to_assets, sprite_file_type):

        """
        Constructor for GetImages class.

        Args:
            path_to_assets (string): The file path pointing to the assets folder.
            sprite_file_type (string): The file extension of the images to be loaded
        """

        self.path_to_assets = path_to_assets
        self.sprite_file_type = sprite_file_type

        self.load_all()

    def load_all(self):

        """Loads all component images into their respective lists"""
        
        self.load_components("base")
        self.load_components("legs")
        self.load_components("body")
        self.load_components("hair")
        self.load_components("feet")

    def load_components(self, component):

        """
        Loads all the files of sprite_file_type into a list. Due to the use of the component argument for both the filepath and class property,
        it is important that the names of the component image folders and the component lists in this class are consistent.        

        Args:
            component (string): The component images to be loaded, eg. Body, feet. This is used to find the correct file path,
                                and also to specifiy which list to add the images to.
        """
        
        path = glob.glob(self.path_to_assets + "/Sprites/" + component + "/*" + self.sprite_file_type)

        for filename in path:
            getattr(self, component).append(pygame.image.load(filename))
