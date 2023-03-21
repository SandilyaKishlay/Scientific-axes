import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class AxisRange:
    def __init__(self, start, stop, num=50, transform='linear'):
        """
        Initialize an AxisRange object with the given start and stop values, the number of steps
        between them, and the type of transformation to apply to the values along the axis.
        
        Arguments:
        - start (float): the starting value of the axis range
        - stop (float): the ending value of the axis range
        - num (int, optional): the number of steps between start and stop (default=50)
        - transform (str, optional): the type of transformation to apply to the values along the axis
          (default='linear'). Available options are: 'linear', 'log', 'polar', 'hyperbolic'.
        """
        self.start = start
        self.stop = stop
        self.num = num
        self.transform = transform
        
        # Calculate the axis values based on the given transformation type
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
        """
        Initialize an Axis2D object with the given x and y AxisRange objects, and additional display settings.
        
        Arguments:
        - x_range (AxisRange): an AxisRange object representing the x-axis range
        - y_range (AxisRange): an AxisRange object representing the y-axis range
        - color (str, optional): the color of the axis lines (default='black')
        - width (float, optional): the width of the axis lines (default=1)
        - xlabel (str, optional): the label for the x-axis (default=None)
        - ylabel (str, optional): the label for the y-axis (default=None)
        - title (str, optional): the title for the axis (default=None)
        """
        self.x_range = x_range
        self.y_range = y_range
        self.color = color
        self.width = width
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
    
    def display(self):
        """
        Display the 2D axis using matplotlib.
        """
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
    def init(self, x_range, y_range, z_range, color='black', width=1, xlabel=None, ylabel=None, zlabel=None, title=None):
        """
            Initialize an Axis3D object with the given x, y, and z AxisRange objects, and additional display settings.
            Arguments:
            - x_range (AxisRange): an AxisRange object representing the x-axis range
            - y_range (AxisRange): an AxisRange object representing the y-axis range
            - z_range (AxisRange): an AxisRange object representing the z-axis range
            - color (str, optional): the color of the axis lines (default='black')
            - width (float, optional): the width of the axis lines (default=1)
            - xlabel (str, optional): the label for the x-axis (default=None)
            - ylabel (str, optional): the label for the y-axis (default=None)
            - zlabel (str, optional): the label for the z-axis (default=None)
            - title (str, optional): the title for the axis (default=None)
        """
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
        """
            Display the 3D axis using matplotlib.
        """
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
