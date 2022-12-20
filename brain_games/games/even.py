from random import randint


DESCRIPTION = 'Check and return the answer whether the number is even or not.'


def get_question_and_result():
    number_random = randint(1, 100)
    if number_random % 2 != 0:
        result = "no"
    if number_random % 2 == 0:
        result = "yes"
    question = 'Question: {0}'.format(number_random)
    print(question)
    return question, result
