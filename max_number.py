"""
8. find a maximum of three numbers is given(don't use list)
"""

def max_number():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    if number1 > number2 and number1 > number3:
        print(number1)
    elif number2 > number3:
        print(number2)
    else:
        print(number3)

max_number()
