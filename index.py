from PIL import Image
from utils.spiral_map_pixels import spiral_map_pixels

img = Image.open('img/hylson.png')
img_pixels = img.load()
spiral_map = spiral_map_pixels(img)

for i in spiral_map:
    img.putpixel(i, spiral_map[i])

img.save('img/output.png')
print("Image generated successfully.")