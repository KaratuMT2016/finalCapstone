'''
• A python program that allows the user to access two different financial calculators: 
    • An investment calculator 
    • A home loan repayment calculator.
• Start by creating a python file
• Name the python file finance_calculators.py.py
• Write a comment in the file outlining the steps in writing the code
• Define the menu function
• Define the investment function
• Define the bond function
• Start the program interface
    • Call an instance of the menu()
    • Print an option input
    • Using a while loop when the input is true
    • Depending on the option:
        • call the investment() function
            • choose simple or compound interest
            • input all fields
            • compute the simple and compound interest
            • print the result
        
        • call the bond() function
            • input all fields
            • compute the simple and compound interest
            • print the result

    • Return to the main program interface
    • Enter none to exit the program
    • Display the goodbye message
'''

import math

#============================================MAIN MENU FUNCTION=========================================================
def menu():
    menu_note = '''
                **************************Welcome to the Capstone Project**************************
                Bond         - to calculate the amount you'll have to pay on a home loan
                Investment   - to calculate the amount of interest you'll earn on your investment
                None         - Enter none to exit the program
                '''
    print(menu_note)


#============================================INVESTMENT FUNCTION==========================================================
def investment():

    while True:
        try:

            #The lines of code below takes all the input variables to compute profit on investment.
            deposit_amount = float(input("Please, enter the amount of money to deposit: "))
            interest_rate  = float(input("Enter Interest Rate (%): "))
            investment_no_of_years = int(input("Please, enter number of years you plan investing: "))
            print()

            #This line convert the interest rate value to decimal
            interest_rate = (interest_rate/100)

            #This line take input options 'simple' or 'compound'
            interest_type = input("Please, enter interest type 'Simple' or 'Compound': ").lower()

            #The if...else statement check for meeting criteria 
            if interest_type == "simple":

                print()
                #This computes the simple interest
                period = interest_rate * investment_no_of_years
                simple_interest = deposit_amount * (1 + period)
                simple_profit = f"The simple interest of £{deposit_amount} for a {investment_no_of_years} year investment is £{simple_interest}."
                print(simple_profit)
                print()
                break

            elif interest_type == "compound":
                print()
                #This computes the compound interest
                compound_interest = deposit_amount * math.pow((1 + interest_rate),investment_no_of_years)
                compound_profit = f"The compound interest of £{deposit_amount} for a {investment_no_of_years} year investment is £{round(compound_interest,2)}."
                print(compound_profit)
                print()
                break
            else:
                print()
                print("Please, check to ensure you choose the correct option.")
                print()
            print()
        except Exception as e:
            print()
            print(e)

#=====================================================BOND FUNCTION============================================================================
def bond():
    print()
    while True:
        try:
            #The lines below take all the input variables for computing repayment 
            house_present_value = float(input("Please, enter the present house value amount: "))
            interest_rate  = float(input("Please, enter interest rate (%): "))
            no_repayment_month = int(input("Please, enter bond repayment months: "))
            
            # This converts the percentage to decimal value
            interest_rate = interest_rate/100

            # This converts the annual interest to monthly interest
            monthly_interest_rate = interest_rate/12
            print()

            #The lines of codes below will compute and print the monthly repayment amount using - repay = (i*P)/(1- (1+i)**(-n))
            
            repayment = (monthly_interest_rate * house_present_value)/(1 - math.pow((1 + monthly_interest_rate),(-no_repayment_month)))

            #repayment1 = (monthly_interest_rate * house_present_value)/(1 - (1 + monthly_interest_rate)**(-no_repayment_month))
            
            
            monthly_rate = f"Your monthly repayment amount is £{round(repayment,2)}."
            print(monthly_rate)
            print()
            break

        except Exception as e:
            print(e)
            menu()
#=====================================================PROGRAM INTERFACE========================================================================

#Call an instance of the menu() function
menu()
option = input("Enter either 'Bond' or 'Investment' from the menu above to proceed: ").lower()

#This line takes the investment type and convert it to lower case regardless of the input.
#option = option.lower()

while not option == "none":

    if option == "investment":
        print()
        print("You're now using the investment calculator.")

        #Call an instance of the investment() function
        investment()

    elif option == "bond":
        print()
        print("You're now using the bond calculator.")

        #Call an instance of the bond() function
        bond()

    else:
        print()
        print("Invalid option.")

    print()
    #Call an instance of the menu() function in a loop to display the program interface persistently
    menu()
    option = input("Enter either 'Bond' or 'Investment' from the menu above to proceed: ")
    print()

print()
#This is a goodbye message
print("Thank you for using this calculator. Goodbye!")
print()
#===========================================================================================================================================