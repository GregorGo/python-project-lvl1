from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_example_and_true_answer():
    example = randint(1, 100)
    true_answer = "no" if example % 2 != 0 else "yes"
    return example, true_answer
