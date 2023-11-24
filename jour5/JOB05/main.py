def chiffrement_cesar(texte, decalage):
    texte_chiffre = ""

    for c in texte:
        if 'A' <= c <= 'Z':
            texte_chiffre += chr((ord(c) - 65 + decalage) % 26 + 65)
        elif 'a' <= c <= 'z':
            texte_chiffre += chr((ord(c) - 97 + decalage) % 26 + 97)
        else:
            texte_chiffre += c

    return texte_chiffre

texte_a_chiffrer = "Je suis Gojo sensei, le plus puissant des sorciers de Jujutsu Kaisen"
decalage = 3
texte_chiffre = chiffrement_cesar(texte_a_chiffrer, decalage)

print("Texte original:", texte_a_chiffrer)
print("Texte chiffré:", texte_chiffre)


