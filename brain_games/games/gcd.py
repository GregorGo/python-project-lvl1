from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_result():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    question = 'Question: {} {}'.format(num1, num2)
    print(question)
    if num1 == num2:
        result = num1
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        result = num1
    return question, result
