import random


def start_game():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Welcome To *Spooky* The Number Guessing Game!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

    high_score = 0
# handle errors
    while True:
        solution = random.randint(1, 10)
        tries = 0

        while True:
            guess = input("\nPick a number between 1 and 10, if you dare: ")
            guess = int(guess)
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

        if play_again.lower() == "y":
            print("\nThe current *~high score~* is {}".format(high_score))
            continue
        break

    print("\nToo scared to guess again?! Have it your way! Bwa-ha-ha-ha!\n")


start_game()
