from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_true_result():
    num_random1 = randint(1, 100)
    num_random2 = randint(1, 100)
    question = (f'Question: {num_random1} {num_random2}')
    print(question)
    if num_random1 == num_random2:
        true_result = num_random1
    while num_random1 != num_random2:
        if num_random1 > num_random2:
            num_random1 -=  num_random2
        else:
            num_random2 -= num_random1
        true_result = num_random1
    return str(true_result)
