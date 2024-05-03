# randomGrid.py
import random
from grid import Grid

def randomize_grid(grid: Grid, alive_probability: float = 0.5) -> None:
    """ Randomizes the cells of the given grid based on the specified probability of being alive. """
    for row in range(grid.rows):
        for col in range(grid.cols):
            grid.set_cell(row, col, 1 if random.random() < alive_probability else 0)

if __name__ == "__main__":
    # Example usage: Randomize an existing grid of size 10x10 with approximately 30% cells alive.
    grid = Grid(10, 10)
    randomize_grid(grid, 0.3)
    print("Randomly Initialized Grid:")
    print(grid)
