import numpy as np
import matplotlib.pyplot as plt


def evolve_fractal(Z, c, dt=0.1):
    return Z + dt * (Z**2 + c)


def animate_euler(width, height, c_start, c_end, steps=30):
    x = np.linspace(-2.0, 2.0, width)
    y = np.linspace(-2.0, 2.0, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    c_values = np.linspace(c_start, c_end, steps)

    fig, ax = plt.subplots(figsize=(6, 6))
    for c in c_values:
        Z = evolve_fractal(Z, c)
        fractal = np.abs(Z) < 2
        ax.clear()
        ax.imshow(fractal, cmap='inferno', extent=(-2, 2, -2, 2))
        ax.set_title(f"Fractal Evoluído | c = {c:.3f}")
        plt.pause(0.1)


if __name__ == "__main__":
    animate_euler(400, 400, complex(-0.7, 0.27015), complex(-0.4, 0.6))
