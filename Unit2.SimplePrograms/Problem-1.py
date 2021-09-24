'''Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment 
required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, 
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print:

Remaining balance: 813.41  instead of  Remaining balance: 813.4141998135 

So your program only prints out one thing: the remaining balance at the end of the year in the format:

Remaining balance: 4784.0
'''

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      
# Remaining balance: 361.61

for i in range(12):
    oBalance = balance - balance * monthlyPaymentRate
    balance = oBalance + annualInterestRate/12 * oBalance

print('Remaining balance: {:.2f}'.format(balance))

