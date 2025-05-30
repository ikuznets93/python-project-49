import operator
import random


def calc_game():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator_list = ('+', '-', '*')
    random_operator = random.choice(operator_list)
    question = f'{first_number} {random_operator} {second_number}'
    match random_operator:
        case "+":
            answer = str(operator.add(first_number, second_number))
        case "-":
            answer = str(operator.sub(first_number, second_number))
        case "*":
            answer = str(operator.mul(first_number, second_number))
    return (question, answer)