import numpy as np


A = [0, 1]
B = [2, 0]


POINTS = [
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
]


def reference_transformation(A, B, point):
  A = A[0] + A[1]*1j
  B = B[0] + B[1]*1j
  point = point[0] + point[1]*1j
  z = point - A
  z = z * np.exp(1j*np.angle(B - A))
  return z.real, z.imag


print(reference_transformation(A, B, A))  # [0.0, 0.0]
