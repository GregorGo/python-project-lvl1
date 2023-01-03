from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_true_result():
    num_random1 = randint(10, 100)
    num_random2 = randint(1, 10)
    rand_choice = choice(['+', '-', '*'])
    question = (f'Question: {num_random1} {rand_choice} {num_random2}')
    print(question)
    if rand_choice == '*':
        true_result = num_random1 * num_random2
    elif rand_choice == '+':
        true_result = num_random1 + num_random2
    else:
        true_result = num_random1 - num_random2
    return str(true_result)
