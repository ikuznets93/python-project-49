import brain_games.game_engine.engine as engine
from brain_games.games.calc import calc_game


def main():
    rules = 'What is the result of the expression?'
    num_of_games = 3
        
    name = engine.welcome_user(rules)
    for _ in range(num_of_games):
        question, answer = calc_game()
        engine.ask_question(question)
        user_answer = engine.get_user_answer()
        is_correct_answer = engine.is_correct(answer, user_answer)
        engine.correctness_message(answer, user_answer, is_correct_answer)
        if is_correct_answer is False:
            return engine.failure_message(name)
    engine.congrats_message(name)


if __name__ == "__main__":
    main()