def test():
    input_number = int(input("Enter a number: "))

    while input_number > 0 :
        input_number = int(input_number) % 10

    print(input_number)

test()