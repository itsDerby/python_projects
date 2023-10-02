import random

number = random.randint(1,10)
guess = 0
while guess != number:
    guess = int(input('Enter Guess: '))

    if (guess < number):
        print('Guess Higher!')

    elif(guess > number):
        print('Guess low')
    else:
        print(f'You guessed the number {number} correctly ')

