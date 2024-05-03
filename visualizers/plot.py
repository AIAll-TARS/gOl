

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def visualize_plot(game, generations, sleep_time):
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots()
    game_display = ax.imshow(game.raw_grid, cmap='gray_r')
    ax.set_xticks([])  # Hide x-axis ticks
    ax.set_yticks([])  # Hide y-axis ticks

    button_ax = fig.add_axes([0.81, 0.05, 0.1, 0.075])  # Setup a button
    button = Button(button_ax, 'Close', color='green', hovercolor='orange')
    button.on_clicked(lambda event: plt.close(fig))

    try:
        for _ in range(generations):
            if plt.fignum_exists(fig.number):  # Check if the figure still exists
                game.update()
                game_display.set_data(game.raw_grid)
                plt.draw()
                plt.pause(sleep_time)
            else:
                break  # Exit loop if figure is closed
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.ioff()  # Turn off interactive mode
        if plt.fignum_exists(fig.number):
            plt.close(fig)  # Ensure the figure is closed if still open

    print("Plotting complete or window was closed manually.")

"""


import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation

def visualize_plot(game, generations, sleep_time):
    plt.ion()
    fig, ax = plt.subplots()
    img = ax.imshow(game.raw_grid, cmap='gray_r')
    ax.set_xticks([])
    ax.set_yticks([])

    button_ax = fig.add_axes([0.81, 0.05, 0.1, 0.075])
    button = Button(button_ax, 'Close', color='green', hovercolor='orange')
    button.on_clicked(lambda event: plt.close(fig))

    def update(frame):
        print(f"Updating frame {frame}")  # Debugging statement
        game.update()
        img.set_data(game.raw_grid)
        return img,

    ani = FuncAnimation(fig, update, frames=range(
        generations), repeat=False, blit=True, interval=sleep_time * 1000)

    try:
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        plt.ioff()
        if plt.fignum_exists(fig.number):
            plt.close(fig)
        print("Plotting complete or window was closed manually.")

    print("Animation setup complete.")  # Confirm setup reached
"""