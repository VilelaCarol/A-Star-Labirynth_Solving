
# ON THE MAP FILE:
# 0: empty space (walkable)
# 1: wall (not walkable)
# 2: start position
# 3: goal position
# 4:(.) path (walked)

import argparse

def get_map(map_path):
    lab_matrix = []
    with open(map_path) as f:
        
        for line in f:
            row = line.split(" ")
            
            row = [int(i) for i in row]
            lab_matrix.append(row)

    return lab_matrix

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, lab_matrix):
    neighbors = []
    for i in range(-1, 2): 
        for j in range(-1, 2): 
            if i == 0 and j == 0:
                continue
            if i != 0 and j != 0:
                continue
            row = node[0] + i
            col = node[1] + j
            if row < 0 or row >= len(lab_matrix):
                continue
            if col < 0 or col >= len(lab_matrix[row]):
                continue
            if lab_matrix[row][col] == 1:
                continue
            neighbors.append((row, col))
    return neighbors

def astar(lab_matrix):
    start, goal = None, None
    for i, row in enumerate(lab_matrix):
        for j, cell in enumerate(row):
            if cell == 2:
                start = (i, j)
            elif cell == 3:
                goal = (i, j)
    if start is None or goal is None:
        return []
    
    open_list = [(heuristic(start, goal), 0, start)]  
    came_from = {start: None}  
    cost_so_far = {start: 0}  

    while open_list:
       
        open_list.sort(key=lambda x: x[0])
        current_node = open_list.pop(0)[2]  

        
        if current_node == goal:
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            return path

        for neighbor in get_neighbors(current_node, lab_matrix):
            new_cost = cost_so_far[current_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                open_list.append((priority, new_cost, neighbor))
                came_from[neighbor] = current_node

    return []  


def draw_map(lab_matrix):
    for row in lab_matrix:
        for cell in row:
            if cell == 0:
                print(" ", end="")
            elif cell == 1:
                print("#", end="")
            elif cell == 2:
                print("S", end="")
            elif cell == 3:
                print("G", end="")
            elif cell == 4:
                print(".", end="")
        print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A* algorithm for labyrinth solving.')
    parser.add_argument('map', type=str, help='Path to the map file')
    args = parser.parse_args()
    lab_matrix = get_map(args.map)
    draw_map(lab_matrix)
    print()
    result = astar(lab_matrix)
    for step in result:
        lab_matrix[step[0]][step[1]] = 4
    draw_map(lab_matrix)

