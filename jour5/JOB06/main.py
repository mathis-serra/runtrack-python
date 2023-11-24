def calculate_distance(marches, hauteur):
    distance_cm =(2 * marches)  * hauteur * 7
    distance_m = distance_cm / 100
    return distance_m

marches = int(input("Nombre de marches du phare : "))
hauteur = int(input("Hauteur de chaque marche (en cm) : "))

distance = calculate_distance(marches, hauteur)
print("Pour", marches, "marches de", hauteur, "cm, le gardien parcourt", distance, "m par semaine.")
