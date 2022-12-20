import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game.DESCRIPTION)
    counter = 0
    while counter < 3:
        question, result = game.get_question_and_result()
        char = prompt.string('Your answer: ')
        if str(char) == str(result):
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(.'
                  'Correct answer was "{}".'.format(char, result))
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print('Congratulations, {0}!'.format(name))
