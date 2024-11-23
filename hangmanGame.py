# Hangman game...

import random

def movie():
    film = ["avesham", "naran", "kalki", "home","avatar"]
    word = random.choice(film)
    user = []
    chance = 3

    print("Guess the film!")
    print("Options are", film)

    while True:
        myword = " ".join([letter if letter in user else "_" for letter in word])
        print(myword)
        
        if "_" not in myword:
            print("\tCongrats! You got it right!")
            break

        newword = input("Enter the word : ")

        if newword==word:
            print("Great! You have completed the game.")
            print(f"\tThe film was {word}")
            break

        if len(newword) != 1:
            print("Enter a single letter.")
            continue
        
        if newword in user:
            print("You already guessed that letter!")
            continue

        user.append(newword)

        if newword in word:
            print("Correct letter!")
        else:
            print("Incorrect letter!")
            chance -= 1
            print(f"\tYou have {chance} chances left.")

        if chance == 0:
            print(f"\tSorry! You are out of chances. The film was {word}")
            break

movie()