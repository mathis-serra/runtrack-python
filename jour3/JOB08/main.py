def panier(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")    
    elif type == "fruit" and saison == "été":
        print("Poire, Fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print(" carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("artichaut, aubergine, navet")
    else:
        print("erreur")
panier("fruit", "été")
panier("fruit", "hiver")
