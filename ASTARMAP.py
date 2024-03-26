# include argparse to get the first mandatory arg (map path)

# ON THE MAP FILE:
# 0: empty space (walkable)
# 1: wall (not walkable)
# 2: start position
# 3: goal position
# 4: path (walked)

import argparse

def get_map(map_path):
    lab_matrix = []
    with open(map_path) as f:
        # LOOP THROUGH THE LINES
        for line in f:
            row = line.split(" ")
            # CONVERT STRINGS TO INTS
            row = [int(i) for i in row]
            lab_matrix.append(row)

    return lab_matrix


def astar(lab_matrix):
    # exemplo de retorno esperado
    # return [(2,1),(2,2),(2,3),(1,3)] # coordenadas a partir da posição inicial (Linha, Coluna) - com o ponto de partida e o final inclusos

    return [] # eu coloquei return vetor vazio pq ele não está retornando nada, mas você pode retornar o que quiser no padrão que coloquei no inicio da função

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

