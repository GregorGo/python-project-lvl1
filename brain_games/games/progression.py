from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_example_and_true_answer():
    step = randint(5, 10)
    num1 = randint(1, 5)
    num2 = randint(55, 60)
    numbers = range(num1, num2, step)
    list_num = list(numbers)
    random_index = randint(0, len(list_num) - 1)
    hidden_num = list_num[random_index]
    list_num[random_index] = '..'
    example = " ".join(map(str, list_num))
    true_answer = hidden_num
    return example, str(true_answer)
