"""This module contains the random_game function."""

import prompt

from random import choice, randint


def random_game():
    """Check and return the value of expressions."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What is the result of the expression?')
    counter = 0
    while counter < 3:
        num1 = randint(10, 100)
        num2 = randint(1, 10)
        rand_choice = choice(['+', '-', '*'])
        print('Question: {} {} {}'.format(num1, rand_choice, num2))
        if rand_choice == '*':
            result = num1 * num2
        elif rand_choice == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        char = prompt.string('Your answer: ')
        if str(char) == str(result):
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}".'.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
