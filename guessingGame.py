
###Guessing Game ###
#Importing necessary libraries
import math
import random

#Accepting inputs
lower_bound = int(input("Enter the lower bound:- "))
upper_bound = int(input("Enter the upper bound:- "))

#Generating a guessing number
guess_number = random.randint(lower_bound, upper_bound)

#Initiating the game
print("A random number has now been generated in between the provided bounds!!!")
print("Now you have to guess the number!!")
print("Lets get ready")
input("Press any key to start")

##Guesses##
loop = True
counter = 1
while(loop):
    guess = int(input("Guess the number"))
    if(guess > guess_number):
        print("guess lower and eliminate the range between %d to %d" % (guess, upper_bound))
    if(guess == guess_number):
        print("You guessed in correct number")
        break
    if(guess < guess_number):
        print("guess higher and eliminate the range between %d to %d" % (lower_bound, guess))
    
    counter += 1

print("Congratulations on guessing the game!! You took %d tries" % (counter))
