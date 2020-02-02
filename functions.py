# functions
# import random, sys, os, math
# sys.exit()
# local and global scope


#pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()

#can do code snippets in pythontutor.com/visualize.html#mode=display

def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

def plusOne(number):
    return number + 1

# None value
# end
print('cat', 'dog', 'bird')
print('Hello', 'how', 'are', 'you', sep='ABC')

spam = 42 #global variable

def eggs():
    spam = 42 #local variable
    return spam

print('Some code here.')
print('Some more code.')

def spam():
    print(eggs)

eggs = 42 #global scope
spam()

