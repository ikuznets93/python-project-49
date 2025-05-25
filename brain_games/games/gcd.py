import random


def gcd_game():
    first_number = random.randint(0, 50)
    second_number = random.randint(0, 50)
    question = f'{first_number} {second_number}'
    while first_number > 0 and second_number > 0:
        if first_number >= second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    answer = str(max(first_number, second_number))
    return (question, answer)