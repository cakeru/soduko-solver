# Sudoku Solver and Generator

A Python-based Sudoku application that allows users to generate, solve, and visualize Sudoku puzzles. Leveraging Pygame for an interactive graphical interface, this project provides an engaging way to experience Sudoku solving step-by-step.

## Table of Contents

- Features
- Project Structure
- Installation
- Usage
- How It Works
- Dependencies
- Troubleshooting
- Contributing
- License

## Features

- **Sudoku Puzzle Generation:** Create new Sudoku puzzles with a specified difficulty level.
- **Step-by-Step Solving:** Visualize the solving process in real-time with highlighted cells.
- **Interactive Interface:** User-friendly buttons to randomize puzzles and initiate solving.
- **Unique Solutions:** Ensure that each generated puzzle has only one possible solution.
- **Modular Design:** Organized codebase with separate modules for solving logic, puzzle generation, and display.

## Project Structure

```
sudoku/
├── display.py
├── solver.py
├── logic.py
├── __init__.py
├── requirements.txt
└── README.md
```

- **`display.py`**: Handles the graphical user interface using Pygame.
- **

solver.py

**: Implements the generator-based Sudoku solver using backtracking.
- **

logic.py

**: Manages puzzle generation and ensures uniqueness of solutions.
- **`__init__.py`**: Initializes the package and facilitates module imports.
- **`requirements.txt`**: Lists the project dependencies.
- **`README.md`**: Provides an overview and instructions for the project.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/sudoku-solver.git
   cd sudoku-solver
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**

   ```sh
   python display.py
   ```

2. **Interacting with the Application**

   - **Randomize Button:**
     - **Function:** Generates a new Sudoku puzzle.
     - **Usage:** Click the "Randomize" button to create a fresh puzzle with a unique solution.
   
   - **Solve Button:**
     - **Function:** Starts the animated solving process.
     - **Usage:** Click the "Solve" button to watch the solver work through the puzzle step-by-step.

## How It Works

### 1. Puzzle Generation (

logic.py

)

- **

generate_full_board()

**: Creates a complete Sudoku board by filling it using a backtracking algorithm.
- **

generate_puzzle(board, difficulty)

**: Removes numbers from the full board to create a puzzle, ensuring that the resulting puzzle has only one unique solution.

### 2. Solving Mechanism (

solver.py

)

- **Backtracking Solver**: Implements a generator-based solver that fills empty cells one by one, yielding the board state after each placement.
- **Validation (`is_valid`)**: Ensures that each number placement adheres to Sudoku rules by checking the corresponding row, column, and 3x3 subgrid.

### 3. Visualization (`display.py`)

- **Pygame Interface**: Renders the Sudoku grid, numbers, and interactive buttons.
- **Animated Solving**: Integrates the solver generator to animate the solving process, highlighting the current cell being filled.
- **User Controls**: Allows users to generate new puzzles and initiate solving through intuitive buttons.

## Dependencies

- **Python 3.x**
- **Pygame**: Used for creating the graphical user interface.

   ```sh
   pygame==2.6.1
   ```

*All dependencies are listed in the `requirements.txt` file.*

## Troubleshooting

- **Pygame Installation Issues:**
  - Ensure that you have Python 3 installed.
  - If you encounter issues installing Pygame, refer to the [official Pygame installation guide](https://www.pygame.org/wiki/GettingStarted).

- **Solver Not Working or Crashing:**
  - Verify that the Sudoku puzzle generated has a unique solution.
  - Check the console for any error messages and ensure all modules are correctly imported.

- **Performance Lag During Solving:**
  - Adjust the 

SOLVE_DELAY

 parameter in 

display.py

 to control the speed of the animation.

## Contributing

Contributions are welcome! If you'd like to enhance the project, follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```sh
   git checkout -b feature/EnhancementName
   ```

3. **Commit Your Changes**

   ```sh
   git commit -m "Add some feature"
   ```

4. **Push to the Branch**

   ```sh
   git push origin feature/EnhancementName
   ```

5. **Open a Pull Request**

Please ensure that your contributions adhere to the project's coding standards and include appropriate documentation.

## License

This project is licensed under the MIT License.

---

*Feel free to customize this README further to better fit your project's specific needs and add any additional sections you find necessary.*