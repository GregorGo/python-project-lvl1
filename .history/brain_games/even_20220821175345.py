"""Этот скрипт содержит функцию random_game."""

from random import randint
import prompt

def welcome_user():
    """Это первая наша функция."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def random_game():
    """"Эта функция генерирует случайное число."""
    number_random = randint(1, 100)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: {0}'.format(number_random))
    answer = prompt.string('Your answer: ')
    if (number_random % 2 != 0 and answer == 'no') or (number_random % 2 == 0 and answer == 'yes'):
        print('Correct!')
    elif number_random % 2 != 0 and answer == 'yes':
        print('yes' is wrong answer ;(. Correct answer was 'no'.)
        print('Let\'s try again, {0}!'.format(name))
    elif number_random % 2 == 0 and answer == 'no':
        print('no' is wrong answer ;(. Correct answer was 'yes'.)
        print('Let\'s try again, {0}!'.format(name))






