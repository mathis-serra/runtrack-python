def fruit():
    fruits = ["pomme", "cerise", "orange"]
    fruits = fruits + ["Melon"]
    fruits.insert(2, "Mangue") 
    return fruits

print(fruit())