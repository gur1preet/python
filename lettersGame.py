import random
import os
import sys

#make a list of word
#pick a random worrd
#draw spaces
#take a guess
#draw guess letters and strikes
#print out win/lose

words = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print("Strikes: {}?".format(len(bad_guesses)))
    print("")

    for letter in bad_guesses:
        print(letter,end=' ')
    print("\n\n")

    for letter in secret_word:
            if letter in good_guesses:
                print(letter, end="")
            else:
                print("_",end="")
    print("")


def  get_guess(guesses):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter")
            continue
        elif guess in guesses:
            print("You've already guess that letter")
            continue
        elif not guess.isalpha():
            print("You can only guess letters")
            continue
        else:
            return guess


def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(secret_word)

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses | good_guesses)

        if guess in word_set:
            good_guesses.add(guess)

            if not word_set.symmetric_difference(good_guesses):
                print("You Win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secrt_word))
                done = True

        if done:
            play_again = input("Play again? Y/n").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit: ").lower
    if start == 'q':
        print('Bye')
        sys.exit()
    else:
        return True

print('Welcome to letter guess')

done = False

while True:
    clear()
    welcome()
    play(done)
