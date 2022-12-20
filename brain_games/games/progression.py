from random import choice, randint


DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_result():
    step = randint(5, 10)
    num1 = randint(1, 5)
    num2 = randint(55, 60)
    numbers = tuple(range(num1, num2, step))
    string = " ".join(map(str, numbers))
    number = str(choice(numbers))
    num_of_repl = string.replace(number, '..', 1)
    result = number
    question = 'Question: {}'.format(num_of_repl)
    print(question)
    return question, result
