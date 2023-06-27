def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = ["Banana", "Orange", "Apple", "Mango"]

# Enter favorite fruit
favourite = input("What is your favourite fruit? ")
fruits.insert(0, favourite)

# Enter least favorite fruit
least_favorite = input("Enter the least favorite fruit: ")
fruits.append(least_favorite)

# Print unordered list
print_list(fruits, header="UNORDERED FRUITS")

# Print ordered list
fruits.sort()
print_list(fruits, header="ORDERED FRUITS")

print()
input("Press return to continue ...")
