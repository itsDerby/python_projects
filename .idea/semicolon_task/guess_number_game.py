import random

guessed_number = random.randint(1,10)
guess = int(input('Enter your guess number: '))
while guessed_number != guess:
    guess = int(input('Enter your guess number: '))
    print('You won')