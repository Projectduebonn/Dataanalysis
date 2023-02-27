#print a circle with 3cm radius
import numpy as np
import matplotlib.pyplot as plt
# Create a circle
r = 3
theta = np.linspace(0, 2*np.pi, 100)
x = r*np.cos(theta)
y = r*np.sin(theta)
# Plot the circle
plt.plot(x, y)
plt.axis('equal')
plt.show()
