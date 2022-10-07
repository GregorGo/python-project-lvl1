"""This module contains the function welcome_user."""

import prompt


def welcome_user():
    """Welcomes the user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
