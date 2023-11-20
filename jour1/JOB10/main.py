investisement_initial = 10000
rendement_annuel = 10

gain_annuel = investisement_initial * rendement_annuel / 100
print("Gain annuel initial:", gain_annuel)

investisement_initial += 5000
rendement_annuel += 2

gain_annuel = investisement_initial * rendement_annuel / 100
print("Nouveau Gain annuel:", gain_annuel)

montant_retiré = investisement_initial * 0.1
investisement_initial -= montant_retiré 

rendement_annuel -= 1

gain_annuel = investisement_initial * rendement_annuel / 100
print("Gain annuel final:", gain_annuel)
