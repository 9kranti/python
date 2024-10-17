"""
16. Find a reminder of a given number until it turns to 0 divided by 10
"""


def remainder_zero():
    number = int(input("Please enter the number to get all remainders till it become zero: "))
    # remainder_number = 1
    remainder_number = number % 10
    print(remainder_number)
    if remainder_number > 0:
        while number > 0:
            # print(number)
            number = number/10
            remainder_number = number % 10
            print(remainder_number)

remainder_zero()
