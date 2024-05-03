from fnlCS50PyProj.gOl.visualizers.plot import visualize_plot
from visualizers.console import visualize_console
from rules import birth_rule, lonely_death_rule, stay_alive_rule, over_populate_rule
from game import Game
from grid import Grid
from randomGrid import randomize_grid


ROWS = 1000
COLS = 1000
RULES = [birth_rule, lonely_death_rule, stay_alive_rule, over_populate_rule]
GENERATIONS = 100
SLEEP_TIME = 0.05
OUTPUT_TYPE = "visualizer"  # console | visualizer


def main() -> None:
    grid = Grid(ROWS, COLS)
    # Sets up the grid with a 30% probability for each cell to be alive
    randomize_grid(grid, 0.0333333)

    """""

    # R-pentomino
    grid.set_cell(10, 10, 1)
    grid.set_cell(10, 11, 1)
    grid.set_cell(11, 9, 1)
    grid.set_cell(11, 10, 1)
    grid.set_cell(12, 10, 1)

  

    grid.set_cell(1, 2, 1)
    grid.set_cell(2, 3, 1)
    grid.set_cell(3, 1, 1)
    grid.set_cell(3, 2, 1)
    grid.set_cell(3, 3, 1)

"""

    game = Game(grid, RULES)

    if OUTPUT_TYPE == "visualizer":
        visualize_plot(game, GENERATIONS, SLEEP_TIME)
    elif OUTPUT_TYPE == "console":
        visualize_console(game, GENERATIONS, SLEEP_TIME)


if __name__ == "__main__":
    main()
