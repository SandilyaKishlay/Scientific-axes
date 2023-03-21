import numpy as np
import matplotlib.pyplot as plt
from fury import actor, window
from ranges_calculations import LinearAxis, LogAxis, PolarAxis, HyperbolicAxis, Grid2D, Grid3D, Scatter, Line, Surface, Legend


x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x) * np.exp(-x/10)

xaxis = LinearAxis('x', range=(0, 10), tick_interval=2)
yaxis = LinearAxis('y', range=(-1, 1), tick_interval=0.5)
grid = Grid2D([xaxis, yaxis])


scatter = Scatter(x, y, color='red', size=5, label='data')
line = Line(x, z, color='blue', width=2, label='fit')


grid.add_actor(scatter)
grid.add_actor(line)
legend = Legend([scatter, line])
grid.show()
legend.show()


