import distance

u = [1, 1, 0]
v = [0, -1, 0]

# dist = distance.euclidean(u, v)
# print("Distância Euclidiana:", dist)

# dist = distance.manhattan(u, v)
# print("Distância Manhattan:", dist)

# dist = distance.minkowski(u, v, 1)
# print("Distância Minkowski:", dist)

dist = distance.braycurtis(u, v)
print("Distância Braycurtis:", dist)

dist = distance.canberra(u, v)
print("Distância Canberra:", dist)


dist = distance.chebyshev(u, v)
print("Distância Chebyshev:", dist)
