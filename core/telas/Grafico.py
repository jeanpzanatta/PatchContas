from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class Grafico(FigureCanvas):
    """Apenas um teste para verificar a viabilidade de colocar um gráfico na tela inicial"""
    def __init__(self):
        self.fig = Figure()
        super().__init__(self.fig)
        self.axes = self.fig.add_subplot(111)

        self.plot()

    def plot(self):
        ax = self.figure.add_subplot(111)
        t = np.arange(0.0, 50.0, 0.01)
        v = 0.1 * t + 1.5
        c = 0.07 * t + 0.3
        d = v - c
        ax.plot(t, c, color='Red')
        ax.plot(t, v, color='Blue')
        ax.plot(t, d, color='Green')
        self.draw()


if __name__ == '__main__':
    gr = Grafico()
