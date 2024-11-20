# logic.py
import random
import copy
from solver import solve_generator, find_empty, is_valid

def generate_full_board():
    """Generate a complete and valid Sudoku board."""
    board = [[0 for _ in range(9)] for _ in range(9)]
    fill_board(board)
    return board

def fill_board(board):
    """Recursively fill the board to create a complete Sudoku puzzle."""
    find = find_empty(board)
    if not find:
        return True
    row, col = find

    numbers = list(range(1, 10))
    random.shuffle(numbers)
    for num in numbers:
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if fill_board(board):
                return True

            board[row][col] = 0

    return False

def count_solutions(board, solutions, limit=2):
    """Count the number of solutions for a given board. Stops counting after reaching the limit."""
    find = find_empty(board)
    if not find:
        solutions[0] += 1
        return
    row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            count_solutions(board, solutions, limit)
            board[row][col] = 0
            if solutions[0] >= limit:
                return

def generate_puzzle(board, difficulty=40):
    """Remove numbers from the full board to create a puzzle."""
    puzzle = copy.deepcopy(board)
    cells_removed = 0
    attempts = 0
    max_attempts = difficulty * 5  # Prevent infinite loops

    while cells_removed < difficulty and attempts < max_attempts:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            removed = puzzle[row][col]
            puzzle[row][col] = 0

            # Make a copy to solve and check if the puzzle remains uniquely solvable
            board_copy = copy.deepcopy(puzzle)
            solutions = [0]
            count_solutions(board_copy, solutions, limit=2)
            if solutions[0] != 1:
                # If the puzzle is not uniquely solvable, revert the change
                puzzle[row][col] = removed
                attempts += 1
            else:
                cells_removed += 1
                attempts = 0  # Reset attempts after a successful removal

    if cells_removed < difficulty:
        raise ValueError("Unable to generate a puzzle with the desired difficulty. Try reducing the difficulty.")
    else:
        print(f"Puzzle generated with {cells_removed} cells removed.")
    return puzzle