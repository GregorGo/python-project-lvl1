from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_true_result():
    num_random = randint(1, 100)
    if num_random % 2 != 0:
        true_result = "no"
    if num_random % 2 == 0:
        true_result = "yes"
    question = (f'Question: {num_random}')
    print(question)
    return true_result
