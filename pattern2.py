"""
Program to print following pattern
A
B B
C C C
D D D D
E E E E E
"""

def alphabet_pattern():
    rows = int(input("Enter the number of rows: "))
    start = 64
    for i in range(1,rows+1):
        start += 1
        for x in range(i):
            # print(i)
            letter = chr(start)
            print(letter, end=" ")

        print("")

alphabet_pattern()