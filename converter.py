import random

def number_guess():

    def choose_level():
        while True:
            level = input(
                "Pick a level: (easy 1-10, medium 1-20, hard 1-50): "
            ).lower()

            if level == "easy":
                return 10
            elif level == "medium":
                return 20
            elif level == "hard":
                return 50
            else:
                print("Invalid level. Please choose easy, medium, or hard.")

    while True:  # replay loop

        total_tries = 0

        max_number = choose_level()
        computer_number = random.randint(1, max_number)

        while True:  # guessing loop

            user_number = input(
                f"Enter a number between 1 and {max_number}: "
            )

            try:
                user_number = int(user_number)
            except ValueError:
                print("Please enter a valid number")
                continue

            if user_number == computer_number:
                total_tries += 1
                print("Congratulations! You guessed the number!")
                print(f"You tried {total_tries} times")
                break

            elif user_number < computer_number:
                print("Too low")
                total_tries += 1

            else:
                print("Too high")
                total_tries += 1

        while True:  # replay choice

            play_again = input("Do you want to play again? (y/n): ").lower()

            if play_again == "y":
                break

            elif play_again == "n":
                print("Thank you for playing!")
                return

            else:
                print("Invalid input. Please enter y or n.")


number_guess()