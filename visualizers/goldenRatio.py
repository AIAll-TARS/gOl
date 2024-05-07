import numpy as np
import matplotlib.pyplot as plt


def plot_golden_spiral_different_scales():
    phi = (1 + np.sqrt(5)) / 2
    b = np.log(phi) / np.pi
    theta = np.linspace(0, 2 * np.pi * 10, 1000)

    plt.figure(figsize=(8, 8))
    for a in range(1, 6):
        r = a * np.exp(b * theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        plt.plot(x, y, label=f'a={a}')

    plt.title('Golden Spiral with Different Scaling Factors')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    plt.show()


plot_golden_spiral_different_scales()
