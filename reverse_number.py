"""
4. Reverse the given number
"""
def reverse():
    try:
        number = int(input("Enter the number: "))

        list_number = list(str(number))
        length = len(list_number)
        reverse_list = []

        for number in list_number:
            length = length-1
            get_number=list_number[length]
            reverse_list.append(get_number)
            #print(get_number)
        number_new = "".join(reverse_list)
        print("Reversed of given number is ", str(number_new))

    except Exception as e:
        print("Please provide the valid values for numbers as error is saying", str(e))

reverse()