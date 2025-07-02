from utils.map_pixels import map_pixels

def spiral_map_pixels(img):
    map = map_pixels(img)
    spiral_map = {}
    width, height = img.width, img.height
    total_pixels = width * height
    
    # Direções na ordem: direita, baixo, esquerda, cima
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 0
    
    # Começar no centro
    x = width // 2
    y = height // 2
    
    # Usar um conjunto para verificação mais rápida
    visited = set()
    visited.add((x, y))
    
    # Pré-alocar a lista de visitados
    visited_order = [(x, y)]
    visited_order.extend([None] * (total_pixels - 1))
    
    steps = 1
    current_step = 0
    step_increase = False
    
    while len(visited_order) < total_pixels:
        dx, dy = directions[direction_index]
        
        for _ in range(steps):
            x += dx
            y += dy
            
            if 0 <= x < width and 0 <= y < height and (x, y) not in visited:
                visited.add((x, y))
                visited_order[len(visited)] = (x, y)  # Usando o tamanho do conjunto como índice
            else:
                # Desfazer o último movimento inválido
                x -= dx
                y -= dy
                break
        
        direction_index = (direction_index + 1) % 4
        current_step += 1
        
        if current_step % 2 == 0:
            steps += 1
    
    # Mapear as coordenadas na ordem espiral
    for idx, coord in enumerate(visited_order):
        if coord in map:  # Isso pode não ser necessário dependendo da implementação do map_pixels
            spiral_map[coord] = map[coord]
        else:
            # Lidar com casos onde a coordenada não está no mapa original
            pass
    
    return spiral_map