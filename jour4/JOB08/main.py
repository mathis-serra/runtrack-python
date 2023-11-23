L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def add_de_deux(L):
    somme_paire = 0  
    for num in L: 
        if num % 2 == 0:
            somme_paire += num  

    return somme_paire

somme_paire = add_de_deux(L)
print("Somme des valeurs paires:", somme_paire)


