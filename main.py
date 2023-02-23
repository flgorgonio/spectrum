import distance

u = [1, 2, 3]
v = [4, 5, 6]

dist = distance.euclidean(u, v)
print("Distância Euclidiana:", dist)

dist = distance.manhattan(u, v)
print("Distância Manhattan:", dist)

dist = distance.minkowski(u, v, 1)
print("Distância Minkowski:", dist)