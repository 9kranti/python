"""
1.Find given number is even or odd
"""
def even_odd():
    try:
        check_number = int(input("Enter the number: "))
        reminder = int(check_number)%2
        #print(reminder)
        #print(type(check_number))
        #if type(check_number) is int:
        if reminder == 0:
            print("{} is a even number".format(check_number))
        else:
            print("{} is a odd number".format(check_number))
        # else:
        #     print("Please provide the integer value")
    except Exception as e:
        print("Please provide valid value")

even_odd()