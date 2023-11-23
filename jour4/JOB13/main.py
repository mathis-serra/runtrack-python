
L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
T = []

for element in L:
    if element not in T:
        T += [element]

print(T)
