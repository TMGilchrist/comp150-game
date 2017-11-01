import random
from sprite import Sprite
from get_images import GetImages


# Specify file type to load and the image directories
sprite_file_type = ".png"
path_to_assets = "../Assets"

# Get the component images
images = GetImages(path_to_assets, sprite_file_type)

# Create new sprite with random component, draw it and save the image to file
# Arguments: Sprite Size (total canvas), baseImage bodyImage, headImage, feetImage, weaponImage


new_sprite = Sprite((16, 16), (0, 0, 0, 0), random.choice(images.base), random.choice(images.legs), random.choice(images.body), random.choice(images.hair), random.choice(images.feet), 0)
new_sprite.draw()
new_sprite.save_with_id(path_to_assets + "\Sprites\CustomSprites", "png")
