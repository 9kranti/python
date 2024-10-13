"""
2. Find given number is divisible by second given number
"""

def division():
    try:
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
        check_remainder = first_number % second_number

        if check_remainder == 0:
            print("{} is completely divisible by {}".format(first_number,second_number))
        else:
            print("{} is not divisible by {}".format(first_number, second_number))
    except Exception as e:
        print("Please provide the valid values for numbers as error is saying", str(e))

division()
