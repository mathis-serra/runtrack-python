
nom = "Anthony"
prix_unitaire = 10.0
quantité_en_stock = 100


print("Nom du produit:", nom)
print("Prix Unitaire:", prix_unitaire)
print("Quantité en stockk:", quantité_en_stock)

quantité_acheter = int(input("Combien souhaitez vous acheter ?: "))
quantité_en_stock -= quantité_acheter


prix_unitaire *= 1.1


print("\ninformation du produit apres inflation:")
print("Nom du produit:", nom)
print("Prix Unitaire:", prix_unitaire)
print("Quantité en stock", quantité_en_stock)
print("Prix total:", prix_unitaire * quantité_acheter, "€")
