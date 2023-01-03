from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_true_result():
    num_random = randint(2, 100)
    divider = 2
    while divider <= (num_random // 2):
        if num_random % divider == 0:
            result = "no"
            break
        else:
            divider += 1
        true_result = "yes"
    question = (f'Question: {num_random}')
    print(question)
    return true_result
