"""
7. Find given number is armstrong or not
"""

def armstrong_number():
    input_number = int(input("Please enter a number: "))
    list_number = list(str(input_number))
    power_number = len(list_number)
    armstrong_list = []
    #print(power)
    for x in list_number:
        #print("x", x)
        powered_number = int(x)**power_number
        armstrong_list.append(powered_number)
        #print(powered_number)
    print(armstrong_list)
    sum_numbers = sum(armstrong_list)
    print(sum_numbers)
    if sum_numbers == input_number:
        print("Given number is armstrong number")
    else:
        print("Given number is not armstrong number")

armstrong_number()