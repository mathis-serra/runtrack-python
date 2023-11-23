L = [7, 11, 42, 39, 2]

compteur = 0
for i in L:
    compteur += 1

for i in range(compteur):
    for j in range(i+1, compteur):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]

print(L)

    
    