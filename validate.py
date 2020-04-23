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