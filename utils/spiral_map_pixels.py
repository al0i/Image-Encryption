from utils.map_pixels import map_pixels

def spiral_map_pixels(img):
    map = map_pixels(img)
    spiral_map = {}

    #Define directions
    right = (1,0)
    up = (0, -1)
    left = (-1, 0)
    down = (0, 1)
    directions = [right, up, left, down]

    #Start in the center
    x = img.width // 2
    y = img.height // 2

    steps = 1

    visiteds = [(x,y)]

    while len(visiteds) < img.width * img.height:
        for i in range(4): #Number of directions
            xDirection, yDirection = directions[i]
            for j in range(steps):
                x += xDirection
                y += yDirection
                print(x, y)
                if 0 <= x < img.width and 0 <= y < img.height:
                    if (x, y) not in visiteds:
                        visiteds.append((x,y))
                else:
                    break
                
                
            if i % 2 == 1:
                steps += 1
    
    cont = 0
    for i in map.values():
        spiral_map[visiteds[cont]] = i
        cont += 1
    
    return spiral_map
