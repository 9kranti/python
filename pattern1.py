"""
Program to print following pattern
A
A B
A B C
A B C D
A B C D E
"""

def alphabet_pattern():
    rows = int(input("Enter the number of rows: "))

    for i in range(1,rows+1):
        start = 65
        for x in range(i):
            # print(i)
            letter = chr(start)
            print(letter, end=" ")
            start+=1
        print("")

alphabet_pattern()