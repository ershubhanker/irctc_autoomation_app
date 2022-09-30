import os
from PIL import Image

factor = 3

che = Image.open('crop.png')
che.show()
px = che.load()
width, height = che.size


img = Image.new('RGB', (width*factor, height*factor), 'Black')
# img.show()
pixels = img.load()
for i in range(width):
    for j in range(height):
        pixels[factor*i, factor*j] = px[i, j]
        pixels[factor*i+1, factor*j] = px[i, j]
        pixels[factor*i+2, factor*j] = px[i, j]

        pixels[factor*i, factor*j+1] = px[i, j]
        pixels[factor*i+1, factor*j+1] = px[i, j]
        pixels[factor*i+2, factor*j+1] = px[i, j]

        pixels[factor*i, factor*j+2] = px[i, j]
        pixels[factor*i+1, factor*j+2] = px[i, j]
        pixels[factor*i+2, factor*j+2] = px[i, j]
        

# img.show()
img.save('crop2.png')