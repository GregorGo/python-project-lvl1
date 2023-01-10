from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_example_and_true_answer():
    num_random1 = randint(1, 100)
    num_random2 = randint(1, 100)
    example = (f'{num_random1} {num_random2}')
    true_answer = str(gcd(num_random1, num_random2))
    return example, true_answer


def gcd(num_random1, num_random2):
    true_answer = math.gcd(num_random1, num_random2)
    return true_answer
