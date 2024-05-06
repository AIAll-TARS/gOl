from visualizers.plot import visualize_plot
from visualizers.console import visualize_console
from rules import birth_rule, lonely_death_rule, stay_alive_rule, over_populate_rule
from game import Game
from grid import Grid
from randomGrid import randomize_grid

ROWS = 100
COLS = 100
RULES = [birth_rule, lonely_death_rule, stay_alive_rule, over_populate_rule]
GENERATIONS = 100
SLEEP_TIME = 0.007
OUTPUT_TYPE = "visualizer"  # console | visualizer
RANDOMIZE = True
ALIVE_PROBABILITY = 0.7


def save_grid_setup(grid: Grid, filename: str) -> None:
    """ Saves the initial setup of the grid in the specified format to a text file. """
    with open(filename, "w") as file:
        for row in range(grid.rows):
            for col in range(grid.cols):
                if grid.is_alive(row, col):
                    file.write(f"grid.set_cell({row}, {col}, 1)\n")


def main() -> None:
    grid = Grid(ROWS, COLS)

    if RANDOMIZE:
        randomize_grid(grid, ALIVE_PROBABILITY)
    else:
        # Predefined setup (this is an example; adapt as necessary)
        grid.set_cell(1, 2, 1)
        grid.set_cell(2, 3, 1)
        grid.set_cell(3, 1, 1)
        grid.set_cell(3, 2, 1)
        grid.set_cell(3, 3, 1)

    # Save the grid setup to a file
    save_grid_setup(grid, "initial_grid_setup.txt")

    print("Initial Grid Setup saved to 'initial_grid_setup.txt'")
    game = Game(grid, RULES)

    if OUTPUT_TYPE == "visualizer":
        visualize_plot(game, GENERATIONS, SLEEP_TIME)
    elif OUTPUT_TYPE == "console":
        visualize_console(game, GENERATIONS, SLEEP_TIME)


if __name__ == "__main__":
    main()
