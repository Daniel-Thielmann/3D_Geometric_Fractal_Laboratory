import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers  # Import correto do 'layers'
from fractal_generator import julia_set
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Criar conjunto de dados
def generate_fractal_dataset(num_samples=1000):
    fractal_images = []
    for i in range(num_samples):
        c = complex(np.random.uniform(-0.8, 0.8), np.random.uniform(-0.8, 0.8))
        fractal = julia_set(64, 64, c)
        fractal_images.append(fractal)

    fractal_images = np.array(fractal_images).astype("float32") / 255.0
    fractal_images = np.expand_dims(fractal_images, axis=-1)
    return fractal_images


def build_autoencoder(input_shape=(64, 64, 1)):
    encoder = keras.Sequential([
        layers.Input(shape=input_shape),
        layers.Conv2D(32, (3, 3), activation="relu", padding="same"),
        layers.MaxPooling2D((2, 2), padding="same"),
        layers.Conv2D(16, (3, 3), activation="relu", padding="same"),
        layers.MaxPooling2D((2, 2), padding="same"),
    ])

    decoder = keras.Sequential([
        layers.Conv2DTranspose(16, (3, 3), activation="relu", padding="same"),
        layers.UpSampling2D((2, 2)),
        layers.Conv2DTranspose(32, (3, 3), activation="relu", padding="same"),
        layers.UpSampling2D((2, 2)),
        layers.Conv2DTranspose(
            1, (3, 3), activation="sigmoid", padding="same"),
    ])

    autoencoder = keras.Model(encoder.input, decoder(encoder.output))
    autoencoder.compile(optimizer="adam", loss="mse")
    return autoencoder


if __name__ == "__main__":
    data = generate_fractal_dataset()
    autoencoder = build_autoencoder()
    autoencoder.fit(data, data, epochs=10, batch_size=32)
    autoencoder.save("models/autoencoder.h5")
