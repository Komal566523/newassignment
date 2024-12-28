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

#we now chnaged contents in working branch

#we changed here again 