import random


def game():
    question = random.randint(1, 100)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
