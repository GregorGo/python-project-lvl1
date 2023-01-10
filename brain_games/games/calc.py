from random import choice, randint
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_question_and_true_result():
    num_random1 = randint(10, 100)
    num_random2 = randint(1, 10)
    operators = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    )
    operator_name, operator_method = choice(operators)
    num_random = (f'{num_random1} {operator_name} {num_random2}')
    true_result = operator_method(num_random1, num_random2)
    return num_random, str(true_result)
