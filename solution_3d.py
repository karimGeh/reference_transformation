import math
import numpy as np


def transform_reference(points):
  A = np.array(points[0])
  points = np.array(points)

  # translate all points to origin (A)
  points = np.array([point - A for point in points])

  # pick only the x and y coordinates
  points_xy_complex = [
      point[0] + point[1]*1j
      for point in points
  ]

  Bxy_complex = points_xy_complex[1]

  # perform a rotation in the x and y plan
  # to align y axis with projection of B in the xy plane
  # (rotation around axe z)
  points_after_z_rotation = [
      point * np.exp(1j*(- np.angle(Bxy_complex) - math.pi/2))
      for point in points_xy_complex
  ]

  # transform back to x, y, z coordinates
  # with the new x and y coordinates after rotation
  points = [
      [z.real, z.imag, points[i][2]]
      for i, z in enumerate(points_after_z_rotation)
  ]

  # pick the y and z coordinates
  points_yz_complex = [
      point[1] + point[2]*1j
      for point in points
  ]

  Byz_complex = points_yz_complex[1]

  # perform a rotation in the y and z plan
  # to align y axis with point B
  # (rotation around axe x)
  points_after_x_rotation = [
      point * np.exp(1j*(- np.angle(Byz_complex) - math.pi))
      for point in points_yz_complex
  ]

  # transform back to x, y, z coordinates
  # with the new y and z coordinates after rotation
  # around axe x
  points = [
      [points[i][0], z.real, z.imag]
      for i, z in enumerate(points_after_x_rotation)
  ]

  return points


if __name__ == "__main__":
  POINTS = [
      (5, 5, 5),
      (8, 1, 5),
      (9, 8, 6),
  ]

  new_points = transform_reference(POINTS)

  for point, new_point in zip(POINTS, new_points):
    print(point, " --> ", np.around(new_point, decimals=5))
