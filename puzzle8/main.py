from puzzle8.board import Board
from puzzle8.Dijkstra import dijkstra
from puzzle8.parser import read_args

def game():
    print("Starting game")

    args = read_args()

    board = Board(args.size)

    print("Puzzle de départ:")
    print(board.show())

    # Solving puzzle.
    initial_state = str(board)
    final_state = "123456780"

    path = dijkstra(initial_state, final_state)

    if path:
        print("Solution trouvée ! Voici les étapes :")
        for step in path:
            step_list = []
            for i in range(len(step)):
                step_list.append(int(step[i]))
            board.numbers = step_list
            print(board.show())
            
    else:
        print("Pas de solution trouvée.")