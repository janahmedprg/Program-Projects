import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit

N = 10
_s = np.random.rand(N)
_t = np.random.rand(N)
_u = np.random.rand(N)
_v = np.random.rand(N)
x = []
y = []
for s, t, u, v in zip(_s, _t, _u, _v):
    x.append(s)
    x.append(u)
    x.append(None)
    y.append(t)
    y.append(v)
    y.append(None)
plt.plot(x, y)
plt.show()
