from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_example_and_true_answer():
    example = randint(1, 100)
    true_answer = is_prime(example)
    if is_prime(example):
        true_answer = "yes"
    else:
        true_answer = "no"
    return example, true_answer


def is_prime(example):
    divider = 2
    while divider <= (example // 2):
        if example % divider == 0:
            return False
        else:
            divider += 1
    return True
