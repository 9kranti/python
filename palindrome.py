"""
5. Find given number is palindrome or not
"""
def palindrome():
    try:
        input_number = int(input("Enter the number to check palindrome: "))

        list_number = list(str(input_number))
        length = len(list_number)
        reverse_list = []
        for numbers in list_number:
            length = length - 1
            reverse_list.append(list_number[length])
        reverse_number = "".join(reverse_list)
        print("Reversed number is ", reverse_number)
        if input_number == int(reverse_number):
            print("Given number is palindrome")
        else:
            print("Given number is not palindrome")
    except Exception as e:
        print("Please give the valid number")

palindrome()