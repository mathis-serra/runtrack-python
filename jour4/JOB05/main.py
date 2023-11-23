L = [1, 2, 3, 4, 5]

print("La liste sans MAJ", L)

print("Seconde value:", L[1])

def update_list(lst):
    lst[3] = lst[2] + lst[4]

update_list(L)
print("Liste MAJ:", L)


print("Derniere value:", L[-1])
