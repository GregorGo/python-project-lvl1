import prompt

from random import choice, randint


def random_game():
    """Find the number of missing in the progression."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('What number is missing in the progression?')
    counter = 0
    while counter < 3:
        step = randint(5, 10)
        num1 = randint(1, 5)
        num2 = randint(55, 60)
        numbers = tuple(range(num1, num2, step))
        string = " ".join(map(str, numbers))
        number = str(choice(numbers))
        num_of_repl = string.replace(number, '..', 1)
        print('Question: {}'.format(num_of_repl))
        result = number
        char = prompt.string('Your answer: ')
        if str(char) == str(result):
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(.'
                  'Correct answer was "{}".'.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
