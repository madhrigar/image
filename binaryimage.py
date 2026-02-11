import random
import uuid
from PIL import Image

width, height = 10, 10

pixels = []
for _ in range(width * height):
    value = random.random()
    pixel = 255 if value >= 0.5 else 0
    pixels.append(pixel)

img = Image.new("L", (width, height))
img.putdata(pixels)


filename = f"{uuid.uuid4()}.png"
img.save(filename)

