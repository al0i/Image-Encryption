def map_pixels(img):
    img_pixels = img.load()
    map = {}

    for y in range(img.height):
        for x in range(img.width):
            map[(x,y)] = img_pixels[x,y]
    return map