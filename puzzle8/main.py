import flet as ft
import time

from puzzle8.board import Board
from puzzle8.Dijkstra import dijkstra
from puzzle8.parser import read_args

def widgets(page: ft.Page, squares):
    page.add(ft.GridView(squares))


def mygame(page):
    print("Starting game")
    page.title = 'Puzzle8 game'

    board = Board(3)

    squares = [ft.TextField(i) for i in board.numbers]

    # Solving puzzle.
    initial_state = str(board)
    final_state = "123456780"

    def solve(event):

        path = dijkstra(initial_state, final_state)
        if path:
            print("Solution trouvée ! Voici les étapes :")
            for step in path:
                step_list = []
                for i in range(len(step)):
                    step_list.append(int(step[i]))
                    squares[i].value = step[i]
                board.numbers = step_list
                print(board.show())
                page.update()
                time.sleep(0.5)

        else:
            print("Pas de solution trouvée.")
    
    header = ft.Row(
        [ft.Text("Puzzle8 game"),
         ft.Button("solve", on_click=solve),
         ]
    )
    grid = ft.GridView(squares, expand=True, runs_count=3)
    bottom = ft.Row([
        ft.Text('bidule')
    ]
    )

    page.add(ft.Column([header, grid, bottom]))


def game():
    ft.app(mygame)