import math
import random


def is_prime(num):
    if num % 2 == 0:
        return num == 2
    for divider in range(3, math.isqrt(num) + 1, 2):
        if num % divider == 0:
            return False
    return True


def prime_game():
    question = random.randint(1, 50)
    is_prime_number = is_prime(question)
    if is_prime_number is True:
        answer = 'yes'
    else:
        answer = 'no'
    return (question, answer)
