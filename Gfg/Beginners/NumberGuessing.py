#Project 1: Number Guessing Game

import random
import math

print("WELCOME TO NUMBER GUESSING GAME \n \n")

lower = int(input("Enter the lower bound:-"))
upper = int(input("Enter the upper bound:-"))

res = random.randint(lower,upper)
print()
print("You have only ",round(math.log(upper-lower + 1,2)), " chances to guess the integer!")

count=0

while count < math.log(upper-lower + 1,2):
    count+=1

    guess = int(input("Guess the number:"))

    if res > guess:
        print("Try Again! You guessed too small")
    elif res < guess:
        print("Try Again! You guessed too high")
    elif res == guess:
        print("Congratulations! You guessed it in ", count, " try")
        break

if count >= math.log(upper-lower + 1,2):
    print("\n The number is %d" % res)
    print("Better Luck Next Time! :D")


