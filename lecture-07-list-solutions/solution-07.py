def even(list):
    if len(list) == 0:
        return None
    return list[::2]


def odd(list):
    if len(list) == 0:
        return None
    return list[1::2]


def print_list(items, header=None):
    # if items is None:
    #     return
    if header != None:
        print(header)
    for item in items:
        print(f"{item}")
    print()


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# numbers = []

numbers_even = even(numbers)

numbers_odd = odd(numbers)

print_list(numbers_even)

print_list(numbers_odd)
