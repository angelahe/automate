import copy

#examples of list

animal = ['cat', 'bat', 'rat', 'elephant']
print(animal[0])

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0][1])

#prints last item in the list
print(spam[0][-1])

#slice
print(animal[0:2])
#print beginning to index 2
print(animal[:2])
#print beginning at 1 to the end
print(animal[1:])

#delete from list
del spam[2]

#len on list too
len([1,2,3])

#append to list
[1,2,3] + [4,5,6]

#break string into list of characters
list('Hello')

#in and not in
'cat' in ['cat', 'bat', 'rat']
'cat' not in animal

###############################
# for loops with lists

for i in range(4):
    print(i)

#is the same as
for i in [0, 1, 2, 3]:
    print(i)

#get a list with even numbers
list(range(0, 100, 2))

#use an index
supplies = ['paper', 'pens', 'flame-throwers', 'staplers']
for i in range(len(supplies)):
    print('index ' + str(i) + ' is ' + supplies[i])

#var swap
a = 'AAA'
b = 'BBB'

a, b = b, a

#increment and decrement
var = 10

var += 1
var -= 1

###############################
# list methods

spam = ['hello', 'hi', 'howdy']
num = spam.index('hello')

#if duplicate values, will return 1st one, error if it doesn't find it
# in place append
spam.append('moose')
spam.insert(1, 'chicken')
# in place delete
spam.remove('moose')
#will give an error if doesn't exist
del spam[0]

#sort lowest to highest, ascii case sort, ie upper case first
spam.sort()
spam.sort(reverse=True)
#can't sort mixed type lists
spam.sort(key = str.lower) #sort in true alphabetical order

#can use slice, index on string
#string is not mutable
#create new string in a slice

spam = [0, 1, 2, 3, 4, 5]
cheese = spam #copies reference to spam, changes to cheese will change spam as a side effect

cheesy = copy.deepcopy(spam)

#line continuation
    spam = ['apples',
            'oranges',
            'lemons']

    money = print('four score and seven ' + \
                  'years ago')