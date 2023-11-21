n = int(input("Entrez un nombre supérieur à 0: "))

while n <= 0:
    n = int(input("Entrez un nombre supérieur à 0: "))

for i in range(1, n+1):
    print("Table de multiplication de ", i)
    for j in range(1, 11):
        print(i, " x", j, " = ", i*j)
    print()
    
    
    
    
