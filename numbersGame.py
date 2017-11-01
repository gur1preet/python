import random

#generate a random no.
#get a no. guess from player
#compare to secret no.
#print hit and miss

def game():
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            guess_num = int(input("Guess a no. between 1 and 10: "))
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            guesses.append(guess_num)
            if guess_num == secret_num:
                print("You got it!. My number was {}".format(secret_num))
                break
            elif guess_num < 1:
                print("{} too low!".format(guess_num))
            elif guess_num > 10:
                print("{} too high!".format(guess_num))
            else:
                print("That's not it!")
    else:
        print("You didn't get it!. My number was {}".format(secret_num))
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()
