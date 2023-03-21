import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 2D Axes
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])  # Example plot
ax.set_xlim(0, 1)  # Set x-axis limits
ax.set_ylim(0, 1)  # Set y-axis limits
ax.set_xlabel('X Label')  # Set x-axis label
ax.set_ylabel('Y Label')  # Set y-axis label
ax.set_title('Title')  # Set plot title
ax.tick_params(axis='both', labelsize=12, colors='black')  # Set tick labels font size and color
ax.spines['top'].set_visible(False)  # Remove top border
ax.spines['right'].set_visible(False)  # Remove right border
ax.spines['bottom'].set_linewidth(2)  # Set x-axis border width
ax.spines['left'].set_linewidth(2)  # Set y-axis border width

# 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot([0, 1], [0, 1], [0, 1])  # Example plot
ax.set_xlim(0, 1)  # Set x-axis limits
ax.set_ylim(0, 1)  # Set y-axis limits
ax.set_zlim(0, 1)  # Set z-axis limits
ax.set_xlabel('X Label')  # Set x-axis label
ax.set_ylabel('Y Label')  # Set y-axis label
ax.set_zlabel('Z Label')  # Set z-axis label
ax.set_title('Title')  # Set plot title
ax.tick_params(axis='both', labelsize=12, colors='black')  # Set tick labels font size and color
ax.xaxis.pane.fill = False  # Remove x-axis background color
ax.yaxis.pane.fill = False  # Remove y-axis background color
ax.zaxis.pane.fill = False  # Remove z-axis background color
ax.xaxis.line.set_lw(2)  # Set x-axis border width
ax.yaxis.line.set_lw(2)  # Set y-axis border width
ax.zaxis.line.set_lw(2)  # Set z-axis border width
