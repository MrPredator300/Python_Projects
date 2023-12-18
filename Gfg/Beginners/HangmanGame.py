# Project 3: The Hangman Game

import random
from collections import Counter

print("WELCOME TO HANGMAN GAME!")
name = str(input("What's your name? "))
print()
print("Good Luck! ",name)

someWords = '''apple banana mango strawberry  
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

# print("word=",word)

chance = len(word) + 2

# print("chance=",chance)

print("You have got ",chance," attemps")

while chance>0:
    for i in word:
        guess = str(input("Enter a character: "))

        if guess in word:
            print(guess)
        else:
            print("The character guessed is wrong!")
            chance-=1
            print("You have got ",chance," tries left")

if chance==0:
    print("You have lost please try again!")
    print("The correct word is: ",word)
else:
    print("Congratulations you have won!")



