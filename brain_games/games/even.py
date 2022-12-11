"""This module contains the random_game function."""

from random import randint

import prompt


def random_game():
    """Check and return the answer whether the number is even or not."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number_random = randint(1, 100)
        if number_random % 2 != 0:
            result = "no"
        if number_random % 2 == 0:
            result = "yes"
        print('Question: {0}'.format(number_random))
        char = prompt.string('Your answer: ')
        if str(char) == str(result):
            print('Correct!')
        else:
            print('''"{}" is wrong answer ;(. Correct answer was "{}".'''.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
