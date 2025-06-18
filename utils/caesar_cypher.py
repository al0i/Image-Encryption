def caesar_cypher(rgb_tuple,shift):
    shift = shift % 3
    if shift == 0:
        return rgb_tuple    
    r = rgb_tuple[0]
    g = rgb_tuple[1]
    b = rgb_tuple[2]
    if shift == 1:
        return (b,r,g)
    elif shift == 2:
        return (g,b,r)
    