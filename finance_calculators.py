# import math

# Create a program which allows the user to choose between an investment calculator and a bond calculator
# The capitalization of the letters of user's input shouldn't matter 
# Show an appropiate error message if the user enters an invalid input

# If the user chooses investment, ask these details from the user: 
# The amount of money being deposited
# Interest rate (without the % sign)
# Number of years planned for investing
# Ask if they want a simple or compound interest

print("Investment - to calculate the amount of interest you'll earn on your investment\
      \nBond - to calculate the amount you'll have to pay on a home loan\
      \n")

user_input = input("Please choose which calculator you would like to use (Investment/Bond): ").lower()

if user_input == "investment":
    print("Please fill out the information below")
    deposit = int(input("The amount of money you would like to deposit: "))
    investment_rate = float(input("The interest rate %: "))
    investment_years = int(input("Number of years you are planning to invest: "))
    interest = input("Please choose compound or simple interest: ").lower()
    
    if interest == "compound": 
        total_compound = deposit * (pow((1 + investment_rate / 100),investment_years))
        print("Compound interest is £", total_compound)
    elif interest == "simple":
        total_simple = deposit *(1 + investment_rate / 100 *investment_years)
        print("Simple interest is £", total_simple)

    
elif user_input == "bond":
    print("Please fill the missing details below.")

    present_house_value = float(input("The present value of the house:"))
    bond_interest = float(input("The interest rate in %:"))
    repay_months = int(input("The number of months you plan to repay the bond: "))
    real_bond_rate = bond_interest / 100 / 12
    repayment = (real_bond_rate * present_house_value)/(1 - (1 + real_bond_rate)**(-repay_months))
    print("You will pay £" + str(repayment) + " each month.")


else:
    print("Please enter a correct value")
    
    
