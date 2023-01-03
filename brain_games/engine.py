import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    counter = 0
    roundCount = 3
    while counter < roundCount:
        true_result = game.get_question_and_true_result()
        answer = prompt.string('Your answer: ')
        if answer == true_result:
            print('Correct!')
        if answer != true_result:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{true_result}"')
            return print("Let\'s try again, {0}!".format(name))
        counter += 1
    print(f'Congratulations, {name}!')
