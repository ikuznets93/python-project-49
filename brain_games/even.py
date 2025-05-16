import random

import prompt


def is_even(number):  
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
    

def even_game(name): 
    number_of_questions = 3

    for _ in range(number_of_questions):
        question_num = random.randint(1, 100)
        answer = is_even(question_num)
        print(f'Question: {question_num}')
        user_answer = prompt.string('Your answer:')
        
        if answer != user_answer.lower():
            return print(f"{user_answer} is wrong answer ;(. "
                         f"Correct answer was {answer}."
                         f"\nLet's try again, {name}!")
        
        print('Correct!')

    print(f'Congratulation, {name}!')
