"""
20. Find second largest number in the list
"""

def second_largest():
    take_input = "yes"
    list_numbers = []
    while take_input == "yes" or take_input == "y":
        numbers = int(input("Please enter the number to get added in list: "))
        take_input = str(input("Do you want to add more?(y/n) ")).lower()
        list_numbers.append(numbers)
    print("List: ", list_numbers)

    list_numbers.sort()
    print("Second largest number in list is ", list_numbers[-2])

second_largest()