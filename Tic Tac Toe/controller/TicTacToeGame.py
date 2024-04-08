
from collections import deque
from model.Board import Board
from model.PlayingPieceX import PlayingPieceX
from model.PlayingPieceO import PlayingPieceO
from model.Player import Player
from typing import List, Tuple

class TicTacToeGame:
    def __init__(self):
        self.players = deque()
        self.game_board = None

    def initialize_game(self):
        # Creating 2 Players
        self.players = deque()
        cross_piece = PlayingPieceX()
        player1 = Player("Player1", cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player("Player2", noughts_piece)

        self.players.extend([player1, player2])

        # Initialize Board
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True
        while no_winner:
            # Take out the player whose turn it is and also put the player back in the queue
            player_turn = self.players.popleft()

            # Get the free space from the board
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            # Read the user input
            print(f"Player: {player_turn.name} Enter row,column: ", end="")
            s = input()
            values = s.split(",")
            input_row = int(values[0])
            input_column = int(values[1])
            # Place the piece
            piece_added_successfully = self.game_board.add_piece(input_row, input_column, player_turn.playing_piece)
            if not piece_added_successfully:
                # Player cannot insert the piece into this cell, player has to choose another cell
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue

            self.players.append(player_turn)

            winner = self.is_there_winner(input_row, input_column, player_turn.playing_piece.piece_type)
            if winner:
                return player_turn.name

        return "tie"

    def is_there_winner(self, row, column, piece_type):
        row_match = all(cell and cell.piece_type == piece_type for cell in self.game_board.board[row])
        column_match = all(self.game_board.board[i][column] and self.game_board.board[i][column].piece_type == piece_type for i in range(self.game_board.size))
        diagonal_match = all(self.game_board.board[i][i] and self.game_board.board[i][i].piece_type == piece_type for i in range(self.game_board.size))
        anti_diagonal_match = all(self.game_board.board[i][self.game_board.size - 1 - i] and self.game_board.board[i][self.game_board.size - 1 - i].piece_type == piece_type for i in range(self.game_board.size))

        return row_match or column_match or diagonal_match or anti_diagonal_match