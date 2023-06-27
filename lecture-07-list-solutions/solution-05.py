def first(list):
    if len(list) == 0:
        return None
    return list[0]

def last(list):
    if len(list) == 0:
        return None
    return list[-1]

def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


fruits = ["Banana", "Orange", "Apple", "Mango"]

fruits.sort()

print("FIRST")
print(first(fruits))

print("LAST")
print(last(fruits))

print()
input("Press return to continue ...")
