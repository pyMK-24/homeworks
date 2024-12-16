import random

def guess_the_number(min_number, max_number, attempts, initial_capital):
    guess_number = random.randint(min_number, max_number)
    capital = initial_capital
    guess_correct = False
    attempts_left = attempts
    attempts = 0

    while not guess_correct and capital > 0:
        attempts += 1
        while True:
            try:
                bid = int(input('Enter your sum bid: '))
                if bid <= 0:
                    print('Please enter a valid number for your bid')
                elif bid > capital:
                    print(f"You don't have enough capital to make that bid. Your remaining capital is {capital} coins.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number for your bid.")

        while True:
            try:
                guess_to = int(input(f'Try {attempts}. Enter your offer: '))
                if guess_to < min_number or guess_to > max_number:
                    print(f"Please guess a number between {min_number} and {max_number}.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number for your bid.")

        if guess_to > guess_number:
            print('My number is smaller.')
        elif guess_to < guess_number:
            print('My number is bigger.')
        else:
            guess_correct = True
            capital += bid
            print(f"Congratulations! You guessed the number {guess_number} after {attempts} attempts.")

        if not guess_correct:
            capital -= bid
            print(f"Sorry, you lost your bid. Your remaining capital is {capital} coins.")

        if capital <= 0:
            print("You ran out of coins. Game over!")
            break

    if guess_correct:
        capital *= 2
        print(f"You won {capital} coins!")
    else:
        print(f"The correct number was {guess_number}. Your final capital is {capital} coins.")
