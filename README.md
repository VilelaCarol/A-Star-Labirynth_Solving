Algoritmo A* para Solução de Labirintos

1. Introdução
O algoritmo A* é uma técnica de busca em grafos que encontra o caminho mais curto entre um ponto inicial e um ponto final. É amplamente utilizado em Inteligência Artificial para solucionar problemas que envolvem encontrar caminhos eficientes em mapas ou labirintos. Este documento descreve a implementação do algoritmo A* em Python para resolver um labirinto.


2. Requisitos
Python: A versão 3.12.3 foi usada para desenvolver e testar o script.
Arquivo de Mapa do Labirinto: 
Deve ser um arquivo de texto em que:
0 - representa um espaço vazio (caminhável),
1 - representa uma parede (não caminhável),
2 - indica a posição inicial,
3 - indica a posição do objetivo.


3. Como executar o script
Para executar o script, use o seguinte comando no terminal: 

 python astarmap.py "maps/mapa*.txt" 
	
	O ‘*’ representa o número do mapa que você deseja executar.


4. Descrição das Funções
‘get_map’(map_path)
Parâmetro: map_path (string) - O caminho para o arquivo contendo o mapa do labirinto.
Retorno: Uma matriz 2D ‘lab_matrix’, representando o labirinto.
Descrição: Essa função carrega o mapa de um labirinto a partir de um arquivo de texto e o converte em uma matriz 2D.

‘heuristic’(a, b)
Parâmetros: a, b (tuplas) - Coordenadas (x, y) dos pontos para calcular a distância.
Retorno: Inteiro representando a distância absoluta entre a e b.
Descrição: -> a[0] e b[0] representam as coordenadas x de a e b
                   -> a[1] e b[1] representam as coordenadas y de a e b
                   ->A função calcula a diferença absoluta entre as coordenadas x de a e b, e entre as coordenadas y de a e b. Isso é feito através da função abs(), que retorna o valor absoluto de um número.

‘get_neighbors’(node, lab_matrix)
Parâmetros:
node (tupla) - Coordenadas do nó atual.
lab_matrix - A matriz representando o labirinto.
Retorno: Retorna a lista ‘neighbors’, que contém as coordenadas de todas as células adjacentes válidas ao nó especificado.
Descrição: -> Uma lista ‘neighbors’ é criada para armazenar as coordenadas dos vizinhos válidos.
                   -> A função itera através das células adjacentes ao ‘node’ usando dois loops ‘for’, cada um variando de -1 a 1. Isso permite verificar todas as células diretamente acima, abaixo, à esquerda e à direita do nó.
                   -> A célula na mesma posição que o ‘node’ i==0 e j==0 é ignorada.
                   -> Movimentos diagonais são excluídos e i!=0 e j!=0 não são permitidos simultaneamente..
                   -> Para cada célula adjacente a função verifica se está dentro dos limites do labirinto e não é uma parede (lab_matrix[row][col] !=1.
                   -> Células que passam por todas as verificações são adicionadas à lista ‘neighbors’ como tuplas (row, col)

‘astar’(lab_matrix)
Parâmetro: lab_matrix - A matriz representando o labirinto.
Retorno: Lista de tuplas representando o caminho do início ao objetivo.
Descrição: -> A função percorre a matriz ‘lab_matrix’ para localizar as células de início (start, marcada com 2) e de objetivo (goal, marcada com 3).Se start ou goal não forem encontrados, a função retorna uma lista vazia, indicando que o caminho não pode ser calculado.
                   -> A função é inicializada com três estruturas para gerenciar diferentes aspectos da busca do caminho: open_list(uma lista que armazena os nós a serem explorados, juntamente com seus custos e prioridade), came_from(rastreia de onde cada nó foi acessado para reconstruir o caminho após alcançar o objetivo) e cost_so_far(registra o custo acumulado para alcançar cada nó).
                   -> Enquanto ‘open_list’ não estiver vazia, o nó com o menor custo estimado é retirado da lista para exploração. Se esse nó é o objetivo, o algoritmo reconstrói o caminho percorrido até o início e o retorna. Caso contrário, o algoritmo explora os vizinhos desse nó, calculando o custo para cada um e atualizando ‘open_list’, ‘came_from’ e ‘cost_so_far’.
                   -> Para cada vizinho do nó atual, a função calcula o novo custo (‘new_cost’) de chegar lá.
                   -> Se o vizinho não foi visitado ou se um caminho mais barato para ele foi encontrado, ele é adicionado ou atualizado na ‘open_list’ com seu novo custo e prioridade (baseada na soma do custo até o momento e a heurística até o objetivo).


‘draw_map’(lab_matrix)
Parâmetro: lab_matrix - A matriz representando o labirinto.
Descrição: -> A função itera sobre cada linha da matriz ‘lab_matrix’. Dentro de cada linha, itera sobre cada célula (cell).
                   -> Para cada célula, verifica o valor e imprime um caractere correspondente:
0 (espaço vazio): imprime um espaço em branco " ".
1 (parede): imprime "#" para representar uma barreira intransponível.
2 (início): imprime "S" para indicar o ponto de partida.
3 (objetivo): imprime "G" para representar o destino.
4 (caminho): imprime "." para mostrar o caminho encontrado pelo algoritmo A*.
                   -> Ao final de cada linha da matriz, print() é chamado para mover a saída para a próxima linha, garantindo que o labirinto seja exibido corretamente no console.


5. Execução do Script
‘if name == ‘__main__’
Descrição: -> Cria um ‘ArgumentParser’ para processar a linha de comando. É definido com uma descrição do que o script faz que é resolver labirintos usando o algoritmo A*.
                   -> ‘parser.add_argument’ define ‘map’ como o argumento necessário para a execução do script.
                   -> Os argumentos da linha de comando são analisados e o caminho do arquivo do mapa é extraído.
                   -> O ‘get_map’ carrega o mapa do labirinto do arquivo especificado e armazena em ‘lab_matrix’. Assim, o ‘draw_map(lab_matrix) desenha o estado inicial do labirinto no console.
                    -> Na execução do algoritmo A* o ‘astar(lab_matrix)’ executa o algoritmo A* no labirinto carregado e retorna o caminho encontrado como uma lista de coordenadas.
                   -> O caminho retornado pelo A* é usado para atualizar ‘lab_matrix’, marcando as células do caminho com 4.
                   -> O ‘draw_map(lab_matrix)’ desenha novamente o labirinto, mostrando o caminho encontrado pelo A*. 


6. Exemplos de Entrada e Saída
A entrada do programa consiste em um arquivo de texto (.txt) que o usuário pode criar, representando um labirinto como uma matriz n x m onde:

1 indica paredes, locais pelos quais não se pode passar.
0 indica espaços disponíveis, por onde o algoritmo pode navegar.
S (start) marca o ponto inicial de onde a busca começa.
G (goal) marca o ponto de destino que o algoritmo tenta alcançar.

Além disso, para facilitar os testes e a demonstração do funcionamento do algoritmo, o programa inclui três mapas padrão. Usuários podem adicionar novos mapas conforme desejarem, apenas seguindo o formato estabelecido e salvando como arquivos ‘.txt’. Esses mapas podem ser selecionados e usados para testar a eficácia e a eficiência do algoritmo A* em diferentes cenários de labirintos.

A saída do programa será a impressão do labirinto no console, mostrando o caminho encontrado do ponto de início (S) ao ponto final (G), marcado com  ‘.’ para o caminho percorrido.

