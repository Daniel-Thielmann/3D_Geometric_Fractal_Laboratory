from src.fractal_generator import generate_fractal_image
from src.euler_method import animate_euler
from src.ml_model import build_autoencoder, generate_fractal_dataset
from src.visualize_3d import plot_fractal_3d
import numpy as np


def main():
    print("Escolha uma opção:")
    print("1 - Gerar Fractal")
    print("2 - Evoluir Fractal com Euler")
    print("3 - Treinar ML para Gerar Fractais")
    print("4 - Visualizar em 3D")

    option = input("Opção: ")

    if option == "1":
        generate_fractal_image()
    elif option == "2":
        animate_euler(400, 400, complex(-0.7, 0.27015), complex(-0.4, 0.6))
    elif option == "3":
        data = generate_fractal_dataset()
        autoencoder = build_autoencoder()
        autoencoder.fit(data, data, epochs=10, batch_size=32)
    elif option == "4":
        fractal = np.load("data/fractals.npy")
        plot_fractal_3d(fractal)
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
