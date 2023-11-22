def signe(nombre):
    if nombre > 0:
        return "positif"
    elif nombre == 0:
        return "nul"
    else:
        return "negatif"
print(signe(-5))