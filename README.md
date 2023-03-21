# Scientific-axes
This API defines a base AxisRange class that represents a range of values on an axis. It has two attributes, start and stop, that define the start and end points of the range. It also has a transform attribute that is used to apply a non-linear transformation to the axis values.

The LinearRange class is a subclass of AxisRange that defines a linear range of values. It does not have a transform attribute since a linear transformation is the default.

The LogRange, PolarRange, and HyperbolicRange classes are subclasses of AxisRange that define non-linear ranges of values. They each have a transform attribute that applies a logarithmic, polar, or hyperbolic transformation to the axis values, respectively.

To use this API, you can create an instance of any of the AxisRange subclasses and pass it to a plotting library, like Matplotlib, that supports non-linear axis transformations.
