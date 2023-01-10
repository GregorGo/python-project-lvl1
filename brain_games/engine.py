import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    roundCount = range(0, 3, 1)
    for round in roundCount:
        example, true_answer = game.get_example_and_true_answer()
        question = (f'Question: {example}')
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        if answer != true_answer:
            print(
                f'"{answer}" is wrong answer ;(.'
                f'Correct answer was "{true_answer}"'
            )
            return print(f'Let\'s try again, {name}!')
    print(f'Congratulations, {name}!')
