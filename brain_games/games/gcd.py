"""This module contains the random_game function."""

import prompt

from random import randint


def random_game():
    """Find the greatest common divisor of given numbers."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        print('Question: {} {}'.format(num1, num2))
        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
            result = num1
        char = prompt.string('Your answer: ')
        if str(char) == str(result):
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}".'.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
