from decouple import config
from logic import guess_the_number


def load_config():
    min_number = config('MIN_NUMBER', cast=int)
    max_number = config('MAX_NUMBER', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    initial_capital = config('INITIAL_CAPITAL', cast=int)
    return min_number, max_number, attempts, initial_capital


def main():
    min_number, max_number, attempts, initial_capital = load_config()

    print("Welcome to the 'Guess the Number' game!")
    print(f'I thought of a number between {min_number} and {max_number}.')

    guess_the_number(min_number, max_number, attempts, initial_capital)


if __name__ == "__main__":
    main()
