"""
6. Find given number is prime or not
"""
def prime_number():
    input_number = int(input("Please enter the number to check whether its prime or not: "))

    if input_number == 0 or input_number == 1:
        print("Given number is not prime number")
    elif input_number == 2:
        print("Given number is prime number")
    else:
        print("test")
        for x in range(2, input_number):
            remainder = input_number % x
            if remainder == 0:
                print("Given number is not a prime number")
                break
        else:
            #this else block referred from internet
            print("Given number is prime number")

prime_number()