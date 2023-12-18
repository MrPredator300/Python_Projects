#Project 2: Word Guessing Game

import random
import math


print("WELCOME TO WORD GUESSING GAME \n")
name = str(input("What is your name? "))
print("Good Luck! ", name)
print("You will get 12 turns to guess the correct word!")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
size = len(word)

# print("size=",size)

print()
print("Guess the characters")
guesses = ''

turns = 12

while turns > 0:
    failed=0

    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed+=1
    
    if failed==0:
        print("You Win")
        print("The word is: ",word)
        break

    print()
    guess = input("guess a character:")

    guesses+=guess

    if guess not in word:
        turns -=1
        print("Wrong")

        print("You have ", + turns, " more guesses")
    
    if turns==0:
        print("You Lose ")
        print("The correct word was", word)


