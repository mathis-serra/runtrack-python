def moyenne(note1, note2, note3):
    eleve = (note1 + note2 + note3) / 3
    if 15 <= eleve <= 20:
        print("Très bon élève")
    elif 11 <= eleve <= 14:
        print("Bon élève")
    elif 8 <= eleve <= 10:
        print("Élève moyen")
    elif 0 <= eleve <= 7:
        print("Élève devant faire des efforts")
    return eleve
    
note1 = float(input("entrer la premiere note: "))
note2 = float(input("Entrer la seconde note: "))
note3 = float(input("Entrer la troisieme note: "))

moyenne_etudiant = moyenne(note1, note2, note3)
print(moyenne_etudiant)
