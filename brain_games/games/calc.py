from random import choice, randint
import operator

DESCRIPTION = 'What is the result of the expression?'


def get_example_and_true_answer():
    num_random1 = randint(10, 100)
    num_random2 = randint(1, 10)
    operators = (
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
    )
    operator_name, operator_method = choice(operators)
    example = (f'{num_random1} {operator_name} {num_random2}')
    true_answer = operator_method(num_random1, num_random2)
    return example, str(true_answer)
