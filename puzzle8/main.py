from puzzle8.board import Board
from puzzle8.Dijkstra import dijkstra
from puzzle8.parser import read_args

def game():
    print("Starting game")

    args = read_args()

    board = Board(args.size)

    etat_initial = str(board)
    print(etat_initial)
    etat_final = "123456780"

    chemin = dijkstra(etat_initial, etat_final)

    if chemin:
        print("Solution trouvée ! Voici les étapes :")
        for etape in chemin:
            print(etape)
    else:
        print("Pas de solution trouvée.")

    return(board.show())