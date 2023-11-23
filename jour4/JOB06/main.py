L = [1, 2, 3, 4, 5]

def inverse_list(L):
    if len(L) == 0:
        return L
    else:
        L[0], L[-1] = L[-1], L[0]
    return L

L = inverse_list(L)
print("Liste après échange:", L)
