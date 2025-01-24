import random
from engine import open_cells, first_open_cell
from lut import LUT


def strategy_dumb(b):
    return first_open_cell(b)


def strategy_random(b):
    return random.choice(open_cells(b))


def strategy_optimal(b):
    # I had the idea of making the board 1d instead of 2d. When it was 2d, the
    # " for i in range(len(lut) " was never getting reached. Ai helped me make the variable into 1d
    # so i could hit the for statement to use the LUT.

    flattened_board = tuple([cell for row in b for cell in row])

    if "X" not in flattened_board and "O" not in flattened_board:
        if flattened_board[4] not in ['X', 'O']:
            return 5
        else:
            return random.choice([1, 3, 7, 9])  # Pick a corner if the center is unavailable

    for i in range(len(LUT)):
        for j in range(len(LUT[i])):
            if flattened_board == LUT[i][j]:  # Compare the flattened board to the LUT entry
                return i + 1  # Return the matching move

    print("If you see this message, the AI does not recognize the current board\n" + str(b))
    return False

