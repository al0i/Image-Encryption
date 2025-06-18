from PIL import Image


from utils.caesar_cypher import caesar_cypher
from utils.map_pixels import map_pixels

def functions_test():
    print("---- CAESAR CYPHER ----")
    rgb = (1,2,3)
    shift = 6
    print(caesar_cypher(rgb, shift))
    print("-----------------------")
    
    print()

    print("----- MAP PIXELS -----")
    img = Image.open('img/img5x5.png')
    print(map_pixels(img))
    print("----------------------")

    print()

functions_test()