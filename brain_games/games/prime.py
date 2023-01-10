from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_true_result():
    num_random = randint(1, 100)
    true_result = is_prime(num_random)
    return num_random, true_result


def is_prime(num_random):
    divider = 2
    while divider <= (num_random // 2):
        if num_random % divider == 0:
            true_result = "no"
            return true_result
        else:
            divider += 1
    true_result = "yes"
    return true_result




