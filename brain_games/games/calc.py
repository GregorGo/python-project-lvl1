from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_result():
    num1 = randint(10, 100)
    num2 = randint(1, 10)
    rand_choice = choice(['+', '-', '*'])
    question = 'Question: {} {} {}'.format(num1, rand_choice, num2)
    print(question)
    if rand_choice == '*':
        result = num1 * num2
    elif rand_choice == '+':
        result = num1 + num2
    else:
        result = num1 - num2
    return question, result
