#This program says hello and asks for my name

print('Hello World!')
print('What is your name?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# len('Al')
# str(26) => '26'
# int('1234') => 1234
# float('3.14') => 3.14
# float(1) => 1.0
name = 'Bob'
if name == 'Alice':
    print('Hi Alice')

