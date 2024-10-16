"""
12. Program to print the following pattern:
A
B C
D E F
G H I J
K L M N O
"""

def alphabet_pattern():
    rows = int(input("Enter the number of rows: "))
    start = 65
    for i in range(1,rows+1):
        for x in range(i):
            letter = chr(start)
            print(letter, end=" ")
            start+=1
        print("")

alphabet_pattern()