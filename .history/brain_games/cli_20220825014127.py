"""This script contains the function welcome_user."""

import prompt


def welcome_user():
    """Welcomes the user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
