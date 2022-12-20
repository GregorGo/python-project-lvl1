from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_result():
    number_random = randint(2, 100)
    divider = 2
    while divider <= (number_random // 2):
        if number_random % divider == 0:
            result = "no"
            break
        else:
            divider += 1
        result = "yes"
    question = 'Question: {0}'.format(number_random)
    print(question)
    return question, result
