import numpy as np


def e_distance(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    distance = np.linalg.norm(a - b)
    return distance


def dotProduct(a, b):
    dp = sum([i * j for (i, j) in zip(a, b)])
    return dp


w = (3, 4, 5)
v = (1, 4, 2)

print(dotProduct(w, v))
print(e_distance(w, v))
