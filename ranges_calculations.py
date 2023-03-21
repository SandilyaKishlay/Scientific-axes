import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class AxisRange:
    def __init__(self, start, stop, num=50, transform='linear'):
        self.start = start
        self.stop = stop
        self.num = num
        self.transform = transform
     
        if self.transform == 'linear':
            self.axis_values = np.linspace(self.start, self.stop, self.num)
        elif self.transform == 'log':
            self.axis_values = np.logspace(np.log10(self.start), np.log10(self.stop), self.num)
        elif self.transform == 'polar':
            theta = np.linspace(0, 2*np.pi, self.num)
            r = np.linspace(self.start, self.stop, self.num)
            self.axis_values = np.vstack((r*np.cos(theta), r*np.sin(theta)))
        elif self.transform == 'hyperbolic':
            self.axis_values = np.linspace(self.start, self.stop, self.num)
            self.axis_values = 1 / self.axis_values

    def __repr__(self):
        return f"AxisRange(start={self.start}, stop={self.stop}, num={self.num}, transform='{self.transform}')"

class Axis2D:
    def __init__(self, x_range, y_range, color='black', width=1, xlabel=None, ylabel=None, title=None):
        self.x_range = x_range
        self.y_range = y_range
        self.color = color
        self.width = width
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
    
    def display(self):
        fig, ax = plt.subplots()
        ax.plot(self.x_range.axis_values, np.zeros_like(self.x_range.axis_values), color=self.color, linewidth=self.width)
        ax.plot(np.zeros_like(self.y_range.axis_values), self.y_range.axis_values, color=self.color, linewidth=self.width)
        
        if self.xlabel is not None:
            ax.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            ax.set_ylabel(self.ylabel)
        if self.title is not None:
            ax.set_title(self.title)
    
        plt.show()
        
class Axis3D:
    def __init__(self, x_range, y_range, z_range, color='black', width=1, xlabel=None, ylabel=None, zlabel=None, title=None):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range
        self.color = color
        self.width = width
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.zlabel = zlabel
        self.title = title

    def display(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.x_range.axis_values, np.zeros_like(self.x_range.axis_values), np.zeros_like(self.x_range.axis_values), color=self.color, linewidth=self.width)
        ax.plot(np.zeros_like(self.y_range.axis_values), self.y_range.axis_values, np.zeros_like(self.y_range.axis_values), color=self.color, linewidth=self.width)
        ax.plot(np.zeros_like(self.z_range.axis_values), np.zeros_like(self.z_range.axis_values), self.z_range.axis_values, color=self.color, linewidth=self.width)
    
        if self.xlabel is not None:
            ax.set_xlabel(self.xlabel)
        if self.ylabel is not None:
            ax.set_ylabel(self.ylabel)
        if self.zlabel is not None:
            ax.set_zlabel(self.zlabel)
        if self.title is not None:
            ax.set_title(self.title)
    
        plt.show()
