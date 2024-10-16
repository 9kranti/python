"""
9. Program to print the following pattern:
     *
    * *
   * * *
  * * * *
 * * * * *
"""

def pyramid_pattern():
    rows = int(input("Enter the number of rows: "))

    for i in range(rows):
        for x in range(rows-i-1):
            print(" ", end="")
        for x in range(i+1):
            print("*", end=" ")
        print("")

pyramid_pattern()