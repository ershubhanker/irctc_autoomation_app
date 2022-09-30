# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"E:\DJANGO\recapcha bypass\logo.png")

# Setting the points for cropped image
left = 0
top = 250
right = 300
bottom = 270

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
image_file1=im1.save("hit.png")
# Shows the image in image viewer
im1.show()
