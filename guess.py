#this is a guess the number game
import random
print('Hello.  What is your name?')
name = input()
secretNumber = random.randint(1,20)
print('well, ' + name + ', I am thinking of a number between 1 and 20')


def getNum():

    while True:
        num = input("Please enter a number ")
        try:
            val = int(num)
            break;
        except ValueError:
            print("This is not a number. Please enter a valid number")
    return val

#ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('take a guess')
    guess = getNum()

    if guess < secretNumber:
        print('your guess is too low.')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break # this condition is the correct guess

if guess == secretNumber:
    print('good job, ' + name + '! you guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('nope the number i was thinking of was ' + str(secretNumber))