"""Этот скрипт содержит функцию random_game."""

from random import randint
import prompt

def random_game():
    """"Эта функция генерирует случайное число."""
    number_random = randint(1, 100)
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < 3:
        print('Question: {0}'.format(number_random))
        char = prompt.string('Your answer: ')
        if (number_random % 2 != 0 and char == 'no') or (number_random % 2 == 0 and char == 'yes'):
            print('Correct!')
        elif number_random % 2 != 0 and char != 'no':
            print(char + ' is wrong answer ;(. Correct answer was "no".')
            print('Let\'s try again, {0}!'.format(name))
        elif number_random % 2 == 0 and char != 'yes':
            print(char + ' is wrong answer ;(. Correct answer was "yes".')
            print('Let\'s try again, {0}!'.format(name))
        counter += 1
        print('Congratulations, ' + name + '!')

        






