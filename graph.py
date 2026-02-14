import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 1000)

y1 = np.abs(x) + np.sqrt(1 - x**2)
y2 = np.abs(x) - np.sqrt(1 - x**2)

plt.figure(figsize=(6,6))
plt.plot(x, y1, label="Upper part")
plt.plot(x, y2, label="Lower part")

plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

plt.title(r"Graph of: $x^2 + (y-|x|)^2 = 1$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()