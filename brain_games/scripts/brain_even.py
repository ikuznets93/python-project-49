from brain_games.even import even_game
from brain_games.name import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game(name)


if __name__ == "__main__":
    main()