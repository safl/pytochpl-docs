import numpy as np


B = np.random.random((10,10))
C = np.random.random((10,10))

A = B + 2.0 * C

for a in np.nditer(A):
    print a
