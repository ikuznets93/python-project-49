import prompt


def welcome_user(rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    print(rules)
    return name


def ask_question(question):
    print(f'Question: {question}')


def get_user_answer():
    return prompt.string('Your answer:')


def is_correct(answer, user_answer):
    return answer == user_answer


def correctness_message(answer, user_answer, is_correct_answer):     
    if is_correct_answer is True:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{answer}'.") 
        

def failure_message(name):
    print(f"Let's try again, {name}!")


def congrats_message(name):
    print(f'Congratulations, {name}!')