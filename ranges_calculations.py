class Range:
    """
    Class to define a range for an axis with support for linear and non-linear transformations.
    """
    def __init__(self, start, stop, transform_func=None):
        self.start = start
        self.stop = stop
        self.transform_func = transform_func

    def transform(self, value):
        """
        Applies the transform function to the given value, if it exists.
        """
        if self.transform_func is not None:
            return self.transform_func(value)
        else:
            return value


class LinearRange(Range):
    """
    Class to define a linear range for an axis.
    """
    def __init__(self, start, stop):
        super().__init__(start, stop, None)


class LogRange(Range):
    """
    Class to define a log range for an axis.
    """
    def __init__(self, start, stop, base=10):
        super().__init__(start, stop, lambda x: np.log(x) / np.log(base))


class PolarRange(Range):
    """
    Class to define a polar range for an axis.
    """
    def __init__(self, start, stop):
        super().__init__(start, stop, lambda x: np.radians(x))


class HyperbolicRange(Range):
    """
    Class to define a hyperbolic range for an axis.
    """
    def __init__(self, start, stop):
        super().__init__(start, stop, lambda x: np.arcsinh(x))


class Axis:
    """
    Class to define an axis with customizable appearance and labeling.
    """
    def __init__(self, range_, color='black', width=1, tick_length=0.02, tick_width=0.005, label=None, label_offset=0.1):
        self.range = range_
        self.color = color
        self.width = width
        self.tick_length = tick_length
        self.tick_width = tick_width
        self.label = label
        self.label_offset = label_offset

    def get_ticks(self):
        """
        Calculates the tick positions and labels for the axis based on its range.
        """
        # Calculate the tick positions
        num_ticks = 5
        tick_values = np.linspace(self.range.start, self.range.stop, num_ticks)
        tick_values_transformed = self.range.transform(tick_values)

        # Calculate the tick labels
        tick_labels = ["{:.2f}".format(tick) for tick in tick_values]

        return tick_values_transformed, tick_labels


class LinearAxis(Axis):
    """
    Class to define a linear axis.
    """
    def __init__(self, start, stop, color='black', width=1, tick_length=0.02, tick_width=0.005, label=None, label_offset=0.1):
        range_ = LinearRange(start, stop)
        super().__init__(range_, color, width, tick_length, tick_width, label, label_offset)


class LogAxis(Axis):
    """
    Class to define a log axis.
    """
    def __init__(self, start, stop, base=10, color='black', width=1, tick_length=0.02, tick_width=0.005, label=None, label_offset=0.1):
        range_ = LogRange(start, stop, base)
        super().__init__(range_, color, width, tick_length, tick_width, label, label_offset)


class PolarAxis(Axis):
    """
         Class to define a polar axis.
    """
    def __init__(self, start, stop, color='black', width=1, tick_length=0.02, tick_width=0.005, label=None, label_offset=0.1):
        range_ = PolarRange(start, stop)
        super().__init__(range_, color, width, tick_length, tick_width, label, label_offset)


class HyperbolicAxis(Axis):
    """
    Class to define a hyperbolic axis.
    """
    def __init__(self, start, stop, color='black', width=1, tick_length=0.02, tick_width=0.005, label=None, label_offset=0.1):
        range_ = HyperbolicRange(start, stop)
        super().__init__(range_, color, width, tick_length, tick_width, label, label_offset)


class Grid:
    """
    Class to define a grid for a set of 2D or 3D axes.
    """
    def __init__(self, x_axis, y_axis, z_axis=None, show_shadows=False, show_perpendiculars=False, shadow_color='gray', perpendicular_color='gray'):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis
        self.show_shadows = show_shadows
        self.show_perpendiculars = show_perpendiculars
        self.shadow_color = shadow_color
        self.perpendicular_color = perpendicular_color

    def get_ticks(self):
        """
        Calculates the tick positions and labels for each axis in the grid.
        """
        ticks = []

        # Calculate the ticks for the x-axis
        x_tick_values_transformed, x_tick_labels = self.x_axis.get_ticks()
        ticks.append((x_tick_values_transformed, x_tick_labels))

        # Calculate the ticks for the y-axis
        y_tick_values_transformed, y_tick_labels = self.y_axis.get_ticks()
        ticks.append((y_tick_values_transformed, y_tick_labels))

        # Calculate the ticks for the z-axis, if it exists
        if self.z_axis is not None:
            z_tick_values_transformed, z_tick_labels = self.z_axis.get_ticks()
            ticks.append((z_tick_values_transformed, z_tick_labels))

        return ticks


class Actor:
    """
    Base class to define an actor with customizable appearance and data to be plotted.
    """
    def __init__(self, color='black', size=1, label=None):
        self.color = color
        self.size = size
        self.label = label

    def plot(self, ax):
        """
        Plots the data for the actor on the given axes.
        """
        pass


class Scatter(Actor):
    """
    Class to define a scatter plot actor.
    """
    def __init__(self, x, y, z=None, color='black', size=1, label=None):
        super().__init__(color, size, label)
        self.x = x
        self.y = y
        self.z = z

    def plot(self, ax):
        """
        Plots the scatter data on the given axes.
        """
        if self.z is None:
            ax.scatter(self.x, self.y, c=self.color, s=self.size, label=self.label)
        else:
            ax.scatter(self.x, self.y, self.z, c=self.color, s=self.size, label=self.label)


class Line(Actor):
    """
    Class to define a line plot actor.
    """
    def __init__(self, x, y, z=None, color='black', width=1, label=None):
                    super().__init__(color, width, label)
        self.x = x
        self.y = y
        self.z = z

    def plot(self, ax):
        """
        Plots the line data on the given axes.
        """
        if self.z is None:
            ax.plot(self.x, self.y, c=self.color, lw=self.width, label=self.label)
        else:
            ax.plot(self.x, self.y, self.z, c=self.color, lw=self.width, label=self.label)


class Surface(Actor):
    """
    Class to define a surface plot actor.
    """
    def __init__(self, x, y, z, color='viridis', label=None):
        super().__init__(None, None, label)
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def plot(self, ax):
        """
        Plots the surface data on the given axes.
        """
        ax.plot_surface(self.x, self.y, self.z, cmap=self.color, linewidth=0, antialiased=True, label=self.label)


class Legend:
    """
    Class to define a legend for actors on a grid.
    """
    def __init__(self, actors, location='best'):
        self.actors = actors
        self.location = location

    def show(self):
        """
        Shows the legend on the grid.
        """
        handles = []
        labels = []

        for actor in self.actors:
            handle = matplotlib.lines.Line2D([], [], c=actor.color, lw=actor.width, marker='o' if isinstance(actor, Scatter) else None, label=actor.label)
            handles.append(handle)
            labels.append(actor.label)

        plt.legend(handles=handles, labels=labels, loc=self.location)
        plt.show()


