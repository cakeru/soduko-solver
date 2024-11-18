# solver.py

def find_empty(board):
    """
    Find an empty cell in the Sudoku board.
    
    Args:
        board (list of list of int): The Sudoku board.
        
    Returns:
        tuple: (row, col) of the empty cell, or None if the board is full.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    """
    Check if placing a number at a given position is valid.
    
    Args:
        board (list of list of int): The Sudoku board.
        num (int): The number to place.
        pos (tuple): (row, col) position.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    row, col = pos

    # Check Row
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    # Check Column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check 3x3 Subgrid
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve_generator(board):
    """
    Generator-based Sudoku solver using backtracking.
    
    Yields:
        list of list of int: The board state after each number placement or removal.
    """
    find = find_empty(board)
    if not find:
        yield [row[:] for row in board]  # Yield a deep copy of the solved board
        return
    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            yield [row[:] for row in board]  # Yield after placing a number

            # Recursively solve the rest of the board
            yield from solve_generator(board)

            # If placing num doesn't lead to a solution, reset the cell
            board[row][col] = 0
            yield [row[:] for row in board]  # Yield after resetting the cell

    return