from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_result():
    number_random = randint(1, 100)
    if number_random % 2 != 0:
        result = "no"
    if number_random % 2 == 0:
        result = "yes"
    question = 'Question: {0}'.format(number_random)
    print(question)
    return question, result
