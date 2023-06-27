fruits = []

while True:
    fruit = input("Guess another fruit?")
    fruit_trim = fruit.replace(" ", "")
    if (fruit_trim == "") or (fruits.count(fruit.lower()) != 0):
        break
    fruits.append(fruit.lower())

print("FRUITS")
for fruit in fruits:
    print(fruit)

print("Your score is: " + str(len(fruits)))
