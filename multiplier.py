import numpy as np
import matplotlib.pyplot as plt

# Generate random walk data
steps = 1000
x = np.cumsum(np.random.randn(steps))
y = np.cumsum(np.random.randn(steps))

# Plotting the random walk with colorful lines
plt.plot(x, y, color='lightblue', alpha=0.7)
plt.title("Random Walk")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Create data for polar coordinates
theta = np.linspace(0, 2*np.pi, 100)
r = np.ones_like(theta)

# Create the polar plot
plt.polar(theta, r, color='orange')
plt.title("Circle in Polar Coordinates")
plt.show()
