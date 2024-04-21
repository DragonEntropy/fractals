import numpy as np
import matplotlib.pyplot as plt

def julia_set(c = -0.835-0.2321j, num_iter = 1, N = 10, X0 = np.array([-2, 2, -2, 2])):
    x0 = X0[0]
    x1 = X0[1]
    y0 = X0[2]
    y1 = X0[3]
    x, y = np.meshgrid(np.linspace(x0, x1, N), np.linspace(y0, y1, N) * 1j)
    z = x + y
    F = np.zeros([N, N])
    for j in range(num_iter):
        z = z ** 2 + c
        index = np.abs(z) < np.inf
        print(index)
        print(F)
        F += index
    return np.linspace(x0, x1, N), np.linspace(y0, y1, N), F
x, y, F = julia_set(c = -0.835-0.2321j, num_iter = 20, N = 10, X0 = np.array([-1.5, 1.5, -1.5, 1.5]))
plt.figure(figsize = (10, 10))
plt.pcolormesh(x, y, F, cmap = "binary")
plt.axis('equal')
plt.axis('off')
plt.show()