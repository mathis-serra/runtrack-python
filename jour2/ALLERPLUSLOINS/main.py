a = float(input("Entrer la taille du cote a: "))
b = float(input("Entrer la taille du cote b: "))
c = float(input("Entrer la taille du cote c: "))

if a + b > c and b + c > a and a + c > b:

    if a == b == c:
        print("Le triangle est equilateral.")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("le triangle est rectangle et isocèle et angle droit.")
        else:
            print("le triangle est rectangle et isocèle")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("Le traingle a un angle droit")
    else:
        print("Le triangle est Isocele.")
else:
    print("Ce n'est pas possible de creer un triangle avec ces valeurs.")
