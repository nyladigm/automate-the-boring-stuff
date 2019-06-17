'''
Write a function named collatz() that has one parameter named number. If number is even, then collatz() should
print number // 2 and return this value. If number is odd, then collatz() should print and return
3 * number + 1.
Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until
the function returns the value 1.
'''



def collatz(number):
    if number % 2 == 0:   # if number is even
        print(number // 2)
        return number // 2
    elif number % 2 == 1:    # if number is odd
        print(3 * number + 1)
        return 3 * number + 1

x = int(input('Please enter an integer:'))    # have the user enter a number
while x != 1:
    x = collatz(x)    # don't forget to assign the function call to a variable so it keeps calling collatz()