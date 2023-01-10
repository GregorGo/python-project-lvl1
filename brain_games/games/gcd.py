from random import randint
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_true_result():
    num_random1 = randint(1, 100)
    num_random2 = randint(1, 100)
    num_random = (f'{num_random1} {num_random2}')
    true_result = str(gcd(num_random1, num_random2))
    return num_random, true_result

def gcd(num_random1, num_random2):
    true_result = math.gcd(num_random1, num_random2)
    return true_result