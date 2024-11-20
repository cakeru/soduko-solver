# display.py

import pygame
import sys
import copy
from solver import solve_generator
from logic import generate_full_board, generate_puzzle

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 540, 750  # Increased height for the buttons and messages
LINE_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
CELL_BG_COLOR = (240, 240, 240)
BUTTON_COLOR = (0, 200, 0)
BUTTON_HOVER_COLOR = (0, 255, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)
CLOSE_BUTTON_COLOR = (200, 0, 0)
CLOSE_BUTTON_HOVER_COLOR = (255, 0, 0)
CLOSE_BUTTON_TEXT_COLOR = (255, 255, 255)
CONGRATS_BG_COLOR = (255, 255, 255, 220)  # Semi-transparent white
CONGRATS_TEXT_COLOR = (0, 128, 0)
CELL_SIZE = WIDTH // 9
FONT = pygame.font.Font(None, 40)
BUTTON_FONT = pygame.font.Font(None, 30)
CONGRATS_FONT = pygame.font.Font(None, 50)

# Animation settings
SOLVE_DELAY = 100  # milliseconds between steps

def draw_grid(screen):
    """Draw the Sudoku grid lines."""
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), thickness)
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)

def draw_numbers(screen, board, highlight=None, initial_board=None):
    """Draw the numbers on the Sudoku grid."""
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                if initial_board and initial_board[i][j] != 0:
                    color = LINE_COLOR  # Pre-filled cells
                    font = FONT
                else:
                    color = (0, 0, 255)  # Solver-filled cells
                    font = pygame.font.Font(None, 35)  # Smaller font for solver
                text = font.render(str(num), True, color)
                text_rect = text.get_rect(center=(j * CELL_SIZE + CELL_SIZE//2, i * CELL_SIZE + CELL_SIZE//2))
                if highlight == (i, j):
                    # Highlight the current cell being tried
                    pygame.draw.circle(screen, (255, 0, 0), (j * CELL_SIZE + CELL_SIZE//2, i * CELL_SIZE + CELL_SIZE//2), CELL_SIZE//2 - 5, 2)
                screen.blit(text, text_rect)

def draw_button(screen, rect, text, font, base_color, hover_color, text_color):
    """Draw a button with hover effect."""
    mouse_pos = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = base_color
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def draw_congrats(screen, ok_button_rect):
    """Draw the Congratulations overlay."""
    # Create a semi-transparent surface
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill(CONGRATS_BG_COLOR)
    screen.blit(overlay, (0, 0))

    # Render the congratulations text
    congrats_text = CONGRATS_FONT.render("Congratulations!", True, CONGRATS_TEXT_COLOR)
    congrats_rect = congrats_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    screen.blit(congrats_text, congrats_rect)

    # Render the OK button
    draw_button(screen, ok_button_rect, "OK", BUTTON_FONT, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR)

def display_sudoku(board, initial_board):
    """Main function to display and interact with the Sudoku game."""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")

    # Define buttons
    button_y = WIDTH + 30
    button_width, button_height = 150, 50
    padding = 20
    random_button_rect = pygame.Rect(padding, button_y, button_width, button_height)
    solve_button_rect = pygame.Rect(WIDTH - button_width - padding, button_y, button_width, button_height)
    close_button_rect = pygame.Rect(WIDTH//2 - button_width//2, button_y, button_width, button_height)

    # Define Congratulations OK button
    ok_button_width, ok_button_height = 100, 50
    ok_button_rect = pygame.Rect(WIDTH//2 - ok_button_width//2, HEIGHT//2 + 30, ok_button_width, ok_button_height)

    solver = None  # Initialize solver generator
    solving = False
    highlight = None  # Current cell being tried
    last_solve_step = 0  # Timestamp of the last solver step
    show_congrats = False  # Flag to show Congratulations window

    clock = pygame.time.Clock()

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and not solving and not show_congrats:
                if random_button_rect.collidepoint(event.pos):
                    try:
                        # Generate a new puzzle
                        full_board = generate_full_board()
                        puzzle = generate_puzzle(full_board, difficulty=40)
                        board[:] = puzzle  # Update the original board
                        initial_board = copy.deepcopy(puzzle)  # Keep track of initial puzzle
                        print("New puzzle generated.")
                    except ValueError as e:
                        print(e)  # Or handle it in the GUI
                if solve_button_rect.collidepoint(event.pos):
                    # Start solving the puzzle
                    solver = solve_generator([row[:] for row in board])
                    solving = True
                    last_solve_step = current_time
                    print("Solver started.")
                if close_button_rect.collidepoint(event.pos):
                    # Close the application
                    running = False

            if show_congrats:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ok_button_rect.collidepoint(event.pos):
                        show_congrats = False  # Dismiss the Congratulations window

        if not show_congrats:
            screen.fill(BG_COLOR)
            draw_grid(screen)
            draw_numbers(screen, board, highlight, initial_board)

            # Draw Buttons
            draw_button(screen, random_button_rect, "Randomize", BUTTON_FONT, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR)
            draw_button(screen, solve_button_rect, "Solve", BUTTON_FONT, BUTTON_COLOR, BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR)
            draw_button(screen, close_button_rect, "Close", BUTTON_FONT, CLOSE_BUTTON_COLOR, CLOSE_BUTTON_HOVER_COLOR, CLOSE_BUTTON_TEXT_COLOR)

            if solving and solver:
                if current_time - last_solve_step >= SOLVE_DELAY:
                    try:
                        # Get the next step from the solver
                        current_board = next(solver)
                        print("Solver step taken.")

                        # Find the difference between current_board and board to highlight
                        difference_found = False
                        for i in range(9):
                            for j in range(9):
                                if board[i][j] != current_board[i][j]:
                                    highlight = (i, j)
                                    board[i][j] = current_board[i][j]
                                    print(f"Updated cell ({i}, {j}) to {board[i][j]}")
                                    difference_found = True
                                    break
                            if difference_found:
                                break
                        else:
                            solving = False  # Puzzle solved
                            show_congrats = True  # Show Congratulations window
                            print("Puzzle solved!")

                        last_solve_step = current_time  # Reset timer

                    except StopIteration:
                        solving = False
                        solver = None
                        show_congrats = True  # Show Congratulations window
                        print("Solver finished.")
                    except Exception as e:
                        solving = False
                        solver = None
                        print(f"An error occurred during solving: {e}")

            pygame.display.flip()
            clock.tick(60)  # Maintain 60 FPS

        else:
            # Display Congratulations Window
            draw_congrats(screen, ok_button_rect)
            pygame.display.flip()
            clock.tick(60)

    pygame.quit()
    sys.exit()

# Example usage
if __name__ == "__main__":
    import copy

    # Generate a solvable puzzle
    try:
        full_board = generate_full_board()
        sudoku_board = generate_puzzle(full_board, difficulty=40)
        initial_puzzle = copy.deepcopy(sudoku_board)
        print("Initial puzzle generated.")
        display_sudoku(sudoku_board, initial_puzzle)
    except Exception as e:
        print(f"An error occurred: {e}")