#   This is a practice program to create a collatz sequence.
#   - Bentley 8/3/2020
#
#

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1


print('Please enter a number greater than 1: ')
try:
    number = int(input())

    while number != 1:
        number = collatz(number)
except ValueError:
    print('This is not an integer.')



