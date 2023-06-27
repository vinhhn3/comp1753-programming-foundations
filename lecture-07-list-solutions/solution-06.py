from random import randint


def print_list(items, header=None):
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


while True:
    input_number = int(input("Enter a number (1 - 10): "))
    if (input_number < 1) or (input_number > 10):
        print("Please enter again ...")
        continue
    break

times_table = []

for i in range(0, 13):
    times_table.append(i * input_number)

print_list(times_table)

print()
input("Press return to continue ...")
