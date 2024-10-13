"""
14. Find compound interest of given principle of 7% with 3 years
"""

def compound_interest():
    principle_amount = int(input("Please enter the principle amount: "))
    rate = 7/100
    tenure = 3

    compound_interest_amount = principle_amount * (1 + rate / 1)**(1*3)
    print("Calculated compound interest is" , compound_interest_amount)

compound_interest()