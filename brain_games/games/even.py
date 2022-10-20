"""This module contains the random_game function."""

from random import randint

from brain_games.games import logic

import prompt


def random_game():
    """Check and return the answer whether the number is even or not."""
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number_random = randint(1, 100)
    print('Question: {0}'.format(number_random))
    
    if number_random % 2 != 0 and char == 'no':
        print('Correct!')
    if number_random % 2 == 0 and char == 'yes':
        print('Correct!')
    elif number_random % 2 != 0 and char != 'no':
        print('"{0}" is wrong answer ;(. Correct answer was "no".'.format(char))
        return print("Let\'s try again, {0}!".format(name))
    elif number_random % 2 == 0 and char != 'yes':
        return print('"{0}" is wrong answer ;(. Correct answer was "yes".'.format(char))
    
