import random
import time

def displayIntro():
    print('You are in a land full of dragons.  In front of you')
    print('you see two caves.  In one cave, the dragon is friendly')
    print('and will share his treasure with you.  The other')
    print('is greedy and hungry, adn will each you on sight')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you!  He opens his jaws...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again?  (yes or no)')
    playAgain = input()

# another kind of while
#break statement
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break

#continue statement
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

#for loops
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

#range ie start, stop (not including that value), step value
print('Numbers by 2')
for i in range (48, 101, 2):
    print('i is now ' + str(i))

for i in range(5, -1, -1):
    print('blastoff in ' + str(i))


