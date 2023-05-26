import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 6001)
y = x ** 3 - x * 3 + 1                   # x3 - 3x + 1

z1 = np.gradient(y, x, edge_order = 2)   # 3x2 - 3
z2 = np.gradient(z1, x, edge_order = 2)  # 6x

plt.plot(x, y)
plt.plot(x, z1)
plt.plot(x, z2)
# plt.savefig('grad.png', dpi=80)
plt.show()
