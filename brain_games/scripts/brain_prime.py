import brain_games.common as common
from brain_games.games.prime import prime_game


def main():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    num_of_games = 3
        
    name = common.welcome_user(rules)
    for _ in range(num_of_games):
        question, answer = prime_game()
        common.ask_question(question)
        user_answer = common.get_user_answer()
        is_correct_answer = common.is_correct(answer, user_answer)
        common.correctness_message(answer, user_answer, is_correct_answer)
        if is_correct_answer is False:
            return common.failure_message(name)
    common.congrats_message(name)


if __name__ == "__main__":
    main()