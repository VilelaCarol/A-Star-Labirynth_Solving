import heapq

def get_initial_board():
        print("Digite o estado inicial do quebra-cabeça 3x3, use 0 para o espaço vazio.")
        initial_board = []
        for i in range(3):  # Três linhas
            row = input(f"Digite a linha {i + 1} com os números separados por espaço: ")
            initial_board.extend([int(n) for n in row.split()])
        return initial_board

        

class PuzzleState:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent
        self.zero_pos = board.index(0)
        self.g = 0 if not parent else parent.g + 1
        self.h = self.heuristic()
        self.f = self.g + self.h
            
        
    def heuristic(self):
        distance = 0
        for i, tile in enumerate(self.board):
            if tile != 0:  # Ignorar o espaço vazio
                # Calcular a posição atual (x, y)
                current_x, current_y = i % 3, i // 3
                # Calcular a posição de destino (target_x, target_y)
                target_x, target_y = (tile - 1) % 3, (tile - 1) // 3
                # Adicionar a distância de Manhattan para esta peça ao total
                distance += abs(current_x - target_x) + abs(current_y - target_y)
        return distance


    def move(self, direction):
        x, y = self.zero_pos % 3, self.zero_pos // 3
        if direction == 'up' and y > 0:
            return self._swap(self.zero_pos, self.zero_pos - 3)
        elif direction == 'down' and y < 2:
            return self._swap(self.zero_pos, self.zero_pos + 3)
        elif direction == 'left' and x > 0:
            return self._swap(self.zero_pos, self.zero_pos - 1)
        elif direction == 'right' and x < 2:
                return self._swap(self.zero_pos, self.zero_pos + 1)
        return None



    def _swap(self, i, j):
        new_board = self.board[:]
        new_board[i], new_board[j] = new_board[j], new_board[i]
        return PuzzleState(new_board, self)

        
    def is_goal(self):
        return self.board == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def __lt__(self, other):
        return self.f < other.f





def astar(initial_board):
    open_list = []
    heapq.heappush(open_list, PuzzleState(initial_board))
    visited = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return current_state  # Retorne o estado se for o estado objetivo

        visited.add(tuple(current_state.board))

            # Gere estados filhos e adicione à fila se não foram visitados
        for direction in ['up', 'down', 'left', 'right']:
            next_state = current_state.move(direction)
            if next_state and tuple(next_state.board) not in visited:
                heapq.heappush(open_list, next_state)

    return None  # Retorne None se não encontrar solução

def reconstruct_path(end_state):
    path = []
    current_state = end_state
    while current_state:
        path.append(current_state.board)
        current_state = current_state.parent
    return path[::-1]


def main():
    initial_board = get_initial_board()
    result = astar(initial_board)
    if result:
        print("Solução encontrada!")
        path = reconstruct_path(result)
        for step in path:
            print(step)
    else:
        print("Nenhuma solução encontrada.")

if __name__ == '__main__':
    main()