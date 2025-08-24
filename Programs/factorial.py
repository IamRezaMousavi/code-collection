"""Created on Tue Apr  6 16:35:53 2021

@author: Mohammad
"""


def factorial(number):
    if number < 0:
        raise ValueError('You must enter a non negative integer')
    factorial = 1
    for num in range(2, number + 1):
        factorial *= num
    return factorial


number = int(input('Type a number: '))
print('Factorial of', number, 'is', factorial(number))
input()
