
numbers = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
rounded_numbers = []


compteur = 0
for i in rounded_numbers:
    compteur += 1

for number in numbers:

    rounded_integer = int(number * 100 + 0.5)

    rounded_number = rounded_integer / 100
   
    rounded_numbers.append(rounded_number)


for i in range(compteur):
    for j in range(i + 1, compteur):
        if rounded_numbers[i] > rounded_numbers[j]:
            rounded_numbers[i], rounded_numbers[j] = rounded_numbers[j], rounded_numbers[i]

print(rounded_numbers)

