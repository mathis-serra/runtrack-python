investisement_initial = 10000
rendement_annuel = 0.1

gain_annuel = investisement_initial * rendement_annuel 
print("Gain annuel initial:", gain_annuel)

investisement_initial += 5000
rendement_annuel += 0.02

gain_annuel = investisement_initial * rendement_annuel 
print("Nouveau Gain annuel:", gain_annuel)

montant_retiré = investisement_initial * 0.1
investisement_initial -= montant_retiré 

rendement_annuel -= 0.01

gain_annuel = investisement_initial * rendement_annuel 
print("Gain annuel final:", gain_annuel)
