import numpy as np

# this variable will be used in the transformation function below
# to round the coordinates of the points so that you dont get something like this:
# (-0.7071067811865476, 0.7071067811865476)
# which is not very readable, instead with enabling rounding you will get:
# (-0.707, 0.707)
enable_rounding = (True, 3)


A = [0, 1]
B = [2, 0]

POINTS = [
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
]


# lets transform everything to complex numbers
A = A[0] + A[1]*1j
B = B[0] + B[1]*1j
POINTS = [p[0] + p[1]*1j for p in POINTS]


# the translation of a complex number z is simply adding
# the coordinates of A to z
def translation(z): return z - A


# to rotate a complex number z with an angle phi,
# we need to multiply z by e^(i*phi)
def rotate(z, angle): return z * np.exp(1j*angle)


# the reference transformation is nothing but a translation
# followed by a rotation
def reference_transformation(z):
  z = translation(z)
  z = rotate(z, np.angle(B - A))
  return z


def complex_to_cartesian(z, enable_rounding=(True, 3)):
  if not enable_rounding[0]:
    return z.real, z.imag
  return round(z.real, enable_rounding[1]), round(z.imag, enable_rounding[1])


# now we can transform the points
NEW_POINTS = [reference_transformation(p) for p in POINTS]

# lets now transform the points back to cartesian coordinates
A = complex_to_cartesian(A)
B = complex_to_cartesian(B)
POINTS = [complex_to_cartesian(p) for p in POINTS]
NEW_POINTS = [complex_to_cartesian(p) for p in NEW_POINTS]

for point, new_point in zip(POINTS, NEW_POINTS):
  print(point, " --> ", new_point)
