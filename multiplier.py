import matplotlib.pyplot as plt
import numpy as np

# Create data for polar coordinates
theta = np.linspace(0, 2*np.pi, 100)
r = np.ones_like(theta)

# Create the polar plot
plt.polar(theta, r, color='orange')
plt.title("Circle in Polar Coordinates")
plt.show()
