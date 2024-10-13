"""
3. Find quotient and remainder of a given number by 10
"""
def quotient_remainder():
    try:
        input_number = int(input("Enter any number to check quotient and remainder by 10: "))

        check_quotient = input_number/10
        check_remainder = input_number % 10

        print("Quotient is {} and remainder is {} when {} is divided by 10".format(check_quotient, check_remainder, input_number))
    except Exception as e:
        print("Please check the number you have provided")
        print(e)

quotient_remainder()