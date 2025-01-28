import numpy as np
import plotly.graph_objects as go
from fractal_generator import julia_set


def plot_fractal_3d(fractal):
    x, y = np.meshgrid(
        np.linspace(-2, 2, fractal.shape[0]), np.linspace(-2, 2, fractal.shape[1]))
    z = fractal

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='inferno')])
    fig.update_layout(title="Fractal 3D Interativo", autosize=True)
    fig.show()


if __name__ == "__main__":
    fractal = julia_set(100, 100, complex(-0.7, 0.27015))
    plot_fractal_3d(fractal)
