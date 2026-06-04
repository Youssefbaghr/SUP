import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 2.1, 0.1)

y = np.exp(x)

plt.plot(x, y)

plt.title("Courbe de y = exp(x)")
plt.xlabel("x")
plt.ylabel("y")

plt.grid(True)

plt.show()