# validation methods using pyinputplus library

import pyinputplus as pyip

# validate age input from user written from scratch
while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}.')

# does not proceed until user enters a number
print('won\'t proceed until you enter a number')
response = pyip.inputNum()
print('number entered was '+ str(response))

# keeps prompting until user enters a number
response2 = pyip.inputInt(prompt='Enter a number ')
print('number entered is ' + str(response2))

# min, max, greaterthan, lessthan keyword args
response3 = pyip.inputNum('Enter num: ', min=4)
print('number entered was '+ str(response3))

response4 = pyip.inputNum('Enter num: ', greaterThan=4)
print('number entered was '+ str(response4))

response5 = pyip.inputNum('Enter num: ', min=4, lessThan=6)
print('number entered was '+ str(response5))

response6 = pyip.inputNum('Enter num: ', min=4, max=6)
print('number entered was '+ str(response6))

# blank input not allowed unless blank=True

response7 = pyip.inputNum('Enter age(optional): ', blank=True)
print('age entered was '+ str(response7))

# limit     limit number of tries
# timeout   how many seconds user has to enter valid input
# default
#
# limit - will raise a RetryLimitException
print('enter a number in a max of 2 tries')
response8 = pyip.inputNum(limit=2)

# limit - will raise a TimeoutException
print('enter a number in a max of 10 seconds')
response9 = pyip.inputNum(timeout=10)

#default keyword will return the default vs raising exception
print('enter a number in a max of 2 tries, or default to N/A')
response10 = pyip.inputNum(limit=2, default='N/A')
print(response10)

# allowRegexes and blockRegexes
print('allow roman numerals')
response11 = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response11)
print('allow lower case roman numerals')
response12 = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print(response12)
print('won\'t accept even numbers')
response13 = pyip.inputNum(blockRegexes=[r'[02468]$'])
print(response13)
print('accepts caterpillar, category, but blocks anything else with cat in it')
response14 = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(response14)

# pass custom validation function to inputCustom()
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
                        (sum(numbersList)))
    return int(numbers)  # Return an int form of numbers.

print('enter a num whose digits add up to ten')
response15 = pyip.inputCustom(addsUpToTen)
print(response15)

# yes or no
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response16 = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print('Thank you.  Have a nice day.')

# yes or no in another language
while True:
    promptES = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
    response17 = pyip.inputYesNo(promptES, yesVal='sí', noVal='no')
    if response17 == 'sí':
        break
print('Gracias.  Qué tengas un buen día.')

# multiplication quiz
