import numpy as np
import matplotlib.pyplot as plt


def julia_set(width, height, c, zoom=1, iterations=300):
    x = np.linspace(-2.0 / zoom, 2.0 / zoom, width)
    y = np.linspace(-2.0 / zoom, 2.0 / zoom, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    fractal = np.zeros(Z.shape, dtype=int)
    for i in range(iterations):
        mask = np.abs(Z) < 2
        Z[mask] = Z[mask] ** 2 + c
        fractal[mask] += 1

    return fractal


def generate_fractal_image():
    width, height = 500, 500
    c = complex(-0.7, 0.27015)
    fractal = julia_set(width, height, c)

    plt.figure(figsize=(6, 6))
    plt.imshow(fractal, cmap='inferno', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title("Conjunto de Julia")
    plt.show()


if __name__ == "__main__":
    generate_fractal_image()
