from model.PlayingPiece import PlayingPiece
from typing import List, Tuple

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None] * size for _ in range(size)]

    def add_piece(self, row, column, playing_piece):
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self) -> List[Tuple[int, int]]:
        free_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] is None]
        return free_cells

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(f"{self.board[i][j].piece_type.value}   ", end="")
                else:
                    print("    ", end="")
                print(" | ", end="")
            print()