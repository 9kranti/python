"""
13. Find the simple interest of a given principle amount on 5.5%
"""

def simple_interest():
    principle_amount = int(input("Please enter principle amount: "))
    tenure = 5
    rate = 5.5/100
    simple_interest = principle_amount * tenure * 5.5/100

    print("Simple interest of principle amount {} for tenure {} yrs with rate 5.5% is {}".format(principle_amount, tenure, simple_interest))

simple_interest()