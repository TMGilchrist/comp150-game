# Sprite Generation and Character Creation README

### Note about file paths. 

Currently the assets folder is accessed via a relative filepath. As long as the file heirachy is not changed it should be fine. The path_to_assets variable is currently
used in both main.py and character_creation.py. This should variable should really be put into a seperate module so both classes can access it and it only needs to be changed
once if the filepath changes.

## Sprite Generation

Running main.py will create a random sprite and save it as a png to the Assets/Sprites/CustomSprites folder.

## Character Creation

Running character creation will open a pygame window that will allow the user to cycle through different components (currently: hair, body, legs) to create a character. 
The index positions of the component lists are saved in a text file so the same components will be shown when the user reopens the window. The blue button at the bottom of the screen will serialize the sprite and close the window. Serializing and deserializing are static methods in Sprite. 

## Buttons

The button.py module contains a basic Button class. Buttons can be instantiated with a size, position and colour, onto a parent surface, and can be passed a list of functions to call when pressed. A variable number of arguments for these functions can also be passed as a list of lists, where each sublist contains the arguments for a given function.

Currently, the message parameter does not do anything as there is no method to display text on the button yet.

## Other Files

sprite_names.txt is a list of the names used to save randomly generated sprites. This ensures each sprite has a unique name. To reset the naming, just delete or empty this file.
player_sprite_data.txt contains the index positions of the component lists during character creation, stored as key - value pairs. e.g. head_list 10

Both these text files will be created if they do not exist.

The Assets folder where the sprites and component images are stored. If this folder moves, the filepaths in the program must be updated!

## TODO

* Incorporate character creation screen into the main game. The exit() function should ideally be changed to open/transition into the game instead of closing the window.
* Clean up create_buttons. Possibly by making a CustomButton which inherits from button with size, colour and functions already set.
* Serialize and deserialize could be generalised, allowing other data aside from Sprites to be saved. Sprite.serialize could inherit from the generalised function.
* path_to_assets variable is used both in main.py and character_creation.py and may need to be used in other modules. Having a module to hold this path would make it easier to referance and quicker to change if the path changes.


