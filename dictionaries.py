import pprint
#dictionary examples

myCat = {'size': 'fat', 'color': 'orange', 'disposition': 'loud'}

myCat['size']
print('My cat has ' + myCat['color'] + ' fur')

#so order doesn't matter
#word and definition pairs
#key error if not found

'name' in myCat
'size' not in myCat

for k in myCat.keys():
    print(k)

for k in myCat.values():
    print(k)

for k, v in myCat.items():
    print(k, v)

#will print the key value pair
for i in myCat.items():
    print(i)

myCat.get('name', '') # will return '' if not found
myCat.get('age', 0) # will return 0 if not found

if 'age' not in myCat:
    myCat['age'] = 8

#or set to default value
myCat.setdefault('name', 'Zoey')

#is a shortcut to make sure the value exists, doesn't change if it does exist

message = 'it was a bright cold day in April and the clocks were striking thirteen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#an escaped giant string
''''''

#pretty print
rjtext = pprint.pformat(count)
print(rjtext)

#data structures
cat = {'name': 'Zophie', 'age': 7, 'color' : 'gray'}

#use this for key value pairs for grid
#'top-L' 'top-M', 'top-R'

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', \
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

pprint.pprint(theBoard)

theBoard['top-L'] = 'O'

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

printBoard(theBoard)

#type
type(theBoard)
type(theBoard['top-R'])
