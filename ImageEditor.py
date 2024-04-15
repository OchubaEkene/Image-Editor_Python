# First, Import the Library
from PIL import Image, ImageEnhance, ImageFilter
import os

# Declare the Path
path = './imgs'  # Folder for unedited images

pathOut = '/editedImgs'  # Folder for edited images

# Load an Image from a file
im = Image.open("")

# Examine the file contents
print(im.format, im.size, im.mode)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    # To Sharpen Image and BW
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

# contrast
factor = 1.5
enhancer = ImageEnhance.Contrast(edit)
edit = enhancer.enhance(factor)

clean_name = os.path.splitext(filename)[0]

# Display the image you just loaded
im.show()

edit.save(f'{pathOut}/{clean_name}_edited.jpg')


# ADD MORE FEATURES USING THE DOCUMENTATION https://pillow.readthedocs.io/en/stable/
