"""This module contains the random_game function."""

from random import randint

import prompt


def random_game():
    """Answer "yes" if given number is prime. Otherwise answer "no"."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        num = 3
        account = 0
        if num == 1 or num == 2 or num == 3:
            result = 'yes'
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                account += 1
            if (account <= 0):
                result = 'yes'
            else:
                result = 'no'
        print('Question: {0}'.format(num))
        char = prompt.string('Your answer: ')
        if str(char) == str(result):
            print('Correct!')
        else:
            print('''"{}" is wrong answer ;(. 
            Correct answer was "{}".'''.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
