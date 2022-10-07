"""This module contains general logic."""

import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

def cycle():
    counter = 0
    while counter < 3:
        char = prompt.string('Your answer: ')

def answer():
    return print("Let\'s try again, {0}!".format(name))
    counter += 1
    print('Congratulations, {0}!'.format(name)) 