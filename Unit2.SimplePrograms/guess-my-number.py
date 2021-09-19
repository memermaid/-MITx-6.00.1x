'''In this problem, you'll create a program that guesses a secret number!
The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). 
The computer makes guesses, and you give it input - is its guess too high or too low? 
Using bisection search, the computer will guess the user's secret number!
'''

l = 0
h = 100
guess = 50

print('Please think of a number between 0 and 100!')
print('Is your secret number {} ?'.format(guess))
ans = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')

while ans != 'c':
    if ans == 'l':
        l = guess
        guess = (l + h) // 2;
        print('Is your secret number {} ?'.format(guess))
        ans = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    elif ans == 'h':
        h = guess
        guess = (l + h) // 2;
        print('Is your secret number {} ?'.format(guess))
        ans = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly. ')
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number {} ?'.format(guess))
        ans = input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly.')

if ans == 'c':
    print("Game over. Your secret number was:", guess)