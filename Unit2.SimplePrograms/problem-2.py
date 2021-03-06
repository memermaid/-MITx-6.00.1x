'''Problem 2 - Paying Debt Off in a Year

Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card 
balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year.
Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment 
for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that 
it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required 
math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 4773
annualInterestRate = 0.2
# Lowest Payment: 440

monthly_interest = annualInterestRate / 12
monthly_payment = 10

updated_balance = balance

while updated_balance > 0:
    updated_balance = balance
    monthly_payment += 10
    for i in range(12):
        unpaid_balance = updated_balance - monthly_payment
        updated_balance = unpaid_balance + unpaid_balance * monthly_interest

print("Lowest payment: ", monthly_payment)