import random


def start_game():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Welcome To *~Spooky~* The Number Guessing Game!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    high_score = 0

    while True:
        solution = random.randint(1, 10)
        tries = 0

        while True:
            guess = input("\nPick a number between 1 and 10, if you dare: ")
            try:
                guess = int(guess)
                if (guess > 10 or guess < 1):
                    raise ValueError
            except ValueError:
                print(
                    "\nThe spell only works if you enter a valid number between 1 and 10, try again!")
                continue
            tries += 1

            if guess < solution:
                print("\nAlas, it is higher, my child!")
            elif guess > solution:
                print("\nAlas, it is lower, my child!")
            else:
                break

        if high_score == 0:
            high_score = tries
        elif high_score > tries:
            high_score = tries

        print("""\nWhat a spooky guess! You are correct!
        It took you {} bone-chilling tries... 
        """.format(tries))

        play_again = input("Do you dare risk another round? [y / n]: ")

        if play_again.lower() == ("y" or "yes"):
            print("\nThe current *~high score~* is {}".format(high_score))
            continue
        break

    print("\nToo *~spooked~* to guess again?! Have it your way! Bwa-ha-ha-ha!\n")


start_game()
