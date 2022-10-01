"""This script contains."""

    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    while counter < 3:
    char = prompt.string('Your answer: ')
    print('"{0}" is wrong answer ;(. Correct answer was "yes".'.format(char))
    return print("Let\'s try again, {0}!".format(name))
    counter += 1
    print('Congratulations, {0}!'.format(name))