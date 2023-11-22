def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            print("Le nombre", nombre, "est pair.")
        else:
            print("Le nombre", nombre, "est impair.")
    else:
        print("Erreur : Veuillez entrer un nombre entier positif.")

# Appels de la fonction pour tester son fonctionnement
verifier_pair_impair(4)
verifier_pair_impair(7)
verifier_pair_impair(0)
verifier_pair_impair(10)
