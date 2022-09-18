"""This script contains the random_game function."""

import prompt

from random import choice, randint


def random_game():
    """Check and return the answer whether the number is even or not."""
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What is the result of the expression?')
    while counter < 3:
        num1 = randint(10, 100)
        num2 = randint(1, 10)
        rand_choice = choice(['+', '-', '*'])
        print('Question: {} {} {}'.format(num1, rand_choice, num2))
        if rand_choice == '*':
            result = num1 * num2
        if rand_choice == '+':
            result = num1 + num2
        if rand_choice == '-':
            result = num1 - num2
        char = prompt.string('Your answer: ')
        if int(char) == int(result):
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}".'.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
