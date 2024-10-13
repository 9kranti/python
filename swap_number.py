"""
18. Swap 2 elements in the list
"""
def swap():
    list_number = [1, 2, 3, 4, 5, 6]
    total = len(list_number)

    i = total - 1
    j = total - 2

    list_number[i], list_number[j] = list_number[j], list_number[i]

    print(list_number)

swap()