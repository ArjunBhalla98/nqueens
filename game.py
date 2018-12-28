import numpy as np


class Game(object):
    """
    Allows an instance of the n-queens problem to be played in the console.

    Parameters:
        - n: The number of queens in the game.
        - board: an 8x8 array of integers. 0 represents an empty square, 1 a filled
        square.
        - locations: a list of tuples of (y, x) co-ordinates. 
        None of the tuples are duplicates.
    """

    def __init__(self, n, init_locs=[]):

        self.n = n
        self.board = np.zeros((8, 8), dtype=int)
        self.locations = init_locs

    def place(self, x, y):
        """
        Place will 'place' a queen in a location on the 8x8 board and return
        True if the placement is successful. Returns False if there already
        exists a queen in that location.

        input: y, x: integer co-ordinates.
        """
        if x > 7 or y > 7 or x < 0 or y < 0:
            return False

        if (y, x) in self.locations:
            return False

        if len(self.locations) >= self.n:
            last_loc = self.locations.pop()
            self.board[last_loc[0]][last_loc[1]] = 0

        self.locations.append((y, x))

        self.board[y][x] = 1

        return True

    def clear_board(self):
        """
        Clear_board removes all queens from the board, and empties locations.
        """

        self.locations = []
        self.board = np.array((8, 8), dtype=int)

    def has_won(self):
        """
        has_won checks the locations of each queen and that each queen has been
        placed, and returns True if the winning condition is satisfied (i.e.
        no queens are within line of sight of each other).
        """

        if len(self.locations) != self.n:
            return False

        all_col_sum = np.sum(self.board, axis=0)

        for y, x in self.locations:
            sum_row = sum(self.board[y])
            sum_col = all_col_sum[x]
            sum_diag = sum(np.diagonal(self.board, x))
            sum_diag_minor = sum(np.diagonal(
                np.rot90(self.board), -self.board.shape[1] + (x + 1) + 1))

            if sum_row > 1 or sum_col > 1 or sum_diag > 1 or sum_diag_minor > 1:
                return False

        return True

    def num_cross(self, x, y):
        """
        num_cross is the number of queens that are crossing paths with a queen
        placed at co-ordinates x and y. x and y are integers between 0 and 7 (inc).
        """
        all_col_sum = np.sum(self.board, axis=0)
        sum_row = sum(self.board[y])
        sum_col = all_col_sum[x]
        sum_diag = sum(np.diagonal(self.board, x))
        sum_diag_minor = sum(np.diagonal(
            np.rot90(self.board), -self.board.shape[1] + (x + 1) + 1))

        return sum_row + sum_col + sum_diag + sum_diag_minor - 4
