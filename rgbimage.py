import random
from PIL import Image

width, height = 64, 64

pixels = []
for _ in range(width * height):
    value = random.random()
    v = int(value * 255)

    pixels.append((
    random.randint(0,255),
    random.randint(0,255),
    random.randint(0,255)
   ))

# Create image from pixels
img = Image.new('RGB', (width, height))
img.putdata(pixels)

# Save the image
img.save('rgbimage.png')
