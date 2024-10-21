import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi
x = np.linspace(0, 2*np.pi, 100)

# Calculate y values as sine of x
y = np.sin(x)

# Plot the graph
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')
plt.show()
