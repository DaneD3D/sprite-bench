import os
from PIL import Image
from itertools import product


# import the folder of images to be used, this folder will be in a subfolder of the project folder called "sprites"
# this folder will be called "sprites" and will contain all the images to be used in the sprite sheet
def fetchImages():
    print("Importing Images... ")

    # get the current working directory
    cwd = os.getcwd()
    # os.chdir(cwd + "/sprites")

    # check to see there is a "sprites" folder
    if os.path.isdir(cwd + "/sprites"):
        # The folder exists
        os.chdir(cwd + "/sprites")
    else:
        # The folder does not exist
        os.mkdir(cwd + "/sprites")
        os.chdir(cwd + "/sprites")

    cwd = os.getcwd()

    imageList = []

    # load the images and place them in an array
    for filename in os.listdir(cwd):
        imageList.append(Image.open(filename))

    print("Images Loaded!")
    return imageList


def inputSpriteSize():
    return input("Enter the size in pixels of each sprite... ")


def exportQuadrants(image, d):
    name, ext = image.filename.split(".")
    ext = image.format.lower()
    w, h = image.size
    dir_out = os.getcwd()
    # check to see there is a "sprites" folder
    if os.path.isdir(cwd + "/{name}"):
        # The folder exists
        os.chdir(cwd + "/{name}")
    else:
        # The folder does not exist
        os.mkdir(cwd + "/{name}")
        os.chdir(cwd + "/{name}")

    grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
    for i, j in grid:
        box = (j, i, j + d, i + d)
        out = os.path.join((dir_out), f"{name}_{i}_{j}.{ext}")
        image.crop(box).save(out)


##################################################################################################################################################
##################################################################################################################################################

# BEGIN MAIN PROGRAM
print("Welcome to Sprite Maker!")

# load the images from the sprites folder.
loadedImages = fetchImages()

# Gather the inputs from the user
d = int(inputSpriteSize())
# default values will be 4x4

cwd = os.getcwd()

if os.path.isdir(cwd + "/exports"):
    # The folder exists
    os.chdir(cwd + "/exports")
else:
    # The folder does not exist
    os.mkdir(cwd + "/exports")
    os.chdir(cwd + "/exports")

for image in loadedImages:
    print(image.filename, image.format, image.size, image.mode)
    exportQuadrants(image, d)

    # TEST parameters [x, y]
    # parameters = [4, 4]
    # numberOfSprites = 4 * 4
    # # numberOfSprites = int(parameters[0]) * int(parameters[1])

    # spriteSizeX = image.size / int(parameters[0])
    # spriteSizeY = image.size / int(parameters[1])

    # spriteArray = []

    # # Create the boxes for the sprites
    # for x in range(numberOfSprites - 1):
    #     if x < 1:
    #         cropQuadrant = [0, 0, spriteSizeX, spriteSizeY]
    #     else:
    #         previousQuadrant = spriteArray[x]
    #         cropQuadrant = [previousQuadrant[0]]
    #         cropQuadrant =

    #     spriteArray.append(cropQuadrant)

# inputSpriteSize()

# Divide the grid into sprites

# box = (100, 100, 400, 400)

# region = im.crop(box)

# region.show()

# im.show()

# print(im.format, im.size, im.mode)

print("Thank you for using Sprite Gen")
