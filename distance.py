from math import sqrt, fabs, pow

def euclidean(u, v):
  if len(u) != len(v):
    return None
  dist = 0
  for i in range(len(u)):
    dist = dist + pow((u[i] - v[i]), 2)
  return sqrt(dist)

def manhattan(u, v):
  if len(u) != len(v):
    return None
  dist = 0
  for i in range(len(u)):
    dist = dist + fabs(u[i] - v[i])
  return dist

def minkowski(u, v, p):
  if len(u) != len(v):
    return None
  dist = 0
  for i in range(len(u)):
    dist = dist + pow(fabs(u[i] - v[i]), p)
  return pow(dist, (1/p))

# Outras distâncias
# https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance
