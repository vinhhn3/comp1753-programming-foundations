from random import randint

fruits = ["Banana", "Orange", "Apple", "Mango"]
name = input("Enter name:")

for i in range(100):
    random_index = randint(0, len(fruits) - 1)
    fruit = fruits[random_index]
    print("Your name is: " + name + ", your favorite fruit is: " + fruit)
