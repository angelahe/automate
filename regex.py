#find and find/replace
import re

#this is the long form
def isPhoneNunber(text): #415-555-1234
    if len(text) != 12:
        return False #not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #no area code
    if text[3] != '-':
        return False #missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

#this is with regex
message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print('Phone number found:' + mo.group()) #will find the phone number in the message

#print('Phone numbers found:' + mo.findall()) #will find all

# re.search
# re.group
# \d regex for numeric digit character

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #this groups the input
mo2 = phoneNumRegex2.search(message)
print('phone #: ' + mo2.group()) #prints the phone number in the string
print('phone #: ' + mo2.group(0))
print('area code: ' + mo2.group(1)) #prints the first group in the string ie area code
print('number: ' + mo2.group(2)) #prints the number
areaCode, mainNumber = mo2.groups()
print('area code ' + areaCode)
print('mainNumber ' + mainNumber)


#add () to phone number like this
message2 = 'my number is (415) 555-2222'
phoneNumRegex3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex3.search(message2)
print('area code :' + mo3.group(1))
print('number :' + mo3.group(2))


#use pipes to match one of several patterns as part of regex

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo4 = batRegex.search('Batmobile lost a wheel')
mo4.group() #will print Batmobile
mo5 = batRegex.search('Batmotorcycle lost a wheel')
# mo5.group() #will give nonetype obj has no attribute
print('pattern matched was '+ mo4.group(1)) #to find which suffix was found

#optional matching with question mark eg (wo)?
batRegex2 = re.compile(r'Bat(wo)?man')
ba1 = batRegex2.search('The Adventures of Batman')
print('found '+ ba1.group())
ba2 = batRegex2.search('The Adventures of Batwoman')
print('found '+ ba2.group())

#optional area code then is...
phoneRegex4 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6 = phoneRegex4.search('my number is 402-333-1212')
print('found phone # ' + mo6.group())
mo7 = phoneRegex4.search('her number is 555-5555')
print('found # without code ' + mo7.group())

# match zero or more with *
batRegex3 = re.compile(r'Bat(wo)*man')
mo8 = batRegex3.search('The Adventures of Batman')
print('found batman: ' + mo8.group())
mo9 = batRegex3.search('The Adventures of Batwoman')
print('found batwoman: ' + mo9.group())
mo10 = batRegex3.search('The Adventures of Batwowowowoman')
print('finds 1+ wo strings: ' + mo10.group())

# matching specific repetitions with braces e.g. (Ha){3}
# range of repetitions (Ha){3,5} will match 3-5 reps of Ha
haRegex = re.compile(r'(Ha){3}')
ha1 = haRegex.search('she said HaHaHa')
print('found Ha x 3 pattern: ' + ha1.group())

# greedy and non greedy matching - greedy by default
# non greedy has ? after it
haString = 'HaHaHaHaHaHaHa'
greedyHaRegex = re.compile(r'(Ha){3,5}')
ha2 = greedyHaRegex.search(haString)
print('Ha x 5 found greedy: ', ha2.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
ha3 = nongreedyHaRegex.search(haString)
print('Ha x 3 found non-greedy: ', ha3.group())

#findall method returns list of strings
phoneNumRegex4 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneString = 'Cell:403-333-2929 Work: 212-555-1010'
foundStrings = phoneNumRegex4.findall(phoneString)
print('finds 2 phone nums and puts in list')
print(*foundStrings, sep = ", ")
# or could print with newline:
# print(*foundStrings, sep = "\n")
# or can use map to convert item to string and then join them
# print(' '.join(map(str, foundStrings)))

# character classes
# matches text with 1+ numeric digits then whitespace then letter/digit/_ chars
xmasRegex = re.compile(r'\d+\s\w+')
print(*xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'), sep = ', ')

# define own character classes with []
# this eg matches any vowel, lower/uppercase
vowelRegex = re.compile(r'[aeiouAEIOU]')
print('vowels found: ')
print(*vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'), sep = ' ')

# can define ranges with hyphen
# [a-zA-Z0-9]

# can define negative character class with ^
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print('all consonants in the string: ')
print(*consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'), sep = '')

# ^ and $ character classes for starts with, ends with, and exactly this
beginsWithHello = re.compile(r'^Hello')
print('search result for begins with hello: ')
print(beginsWithHello.search('Hello, world!'))

endsWithNumber = re.compile(r'\d$')
print('search result for ending with number: ')
print(endsWithNumber.search('Your number is 42'))

# begins and ends with number, ie entire regex must match the regex
wholeStringIsNum = re.compile(r'^\d+$')
print('whole string is a number')
print(wholeStringIsNum.search('1234567890'))

# wildcard . matches all but newline
atRegex = re.compile(r'.at')
print('all matches to strings with *at: ')
print(*atRegex.findall('The cat in the hat sat on the flat mat.'), sep = ' ')

# match with .*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print('first name is ' + mo.group(1))
print('last name is ' + mo.group(2))

# greedy vs non greedy match with .*
nongreedyRegex = re.compile(r'<.*?>')
minMatch = nongreedyRegex.search('<To serve man> for dinner.>')
print('non greedy match')
print(minMatch.group())

greedyRegex = re.compile(r'<.*>')
maxMatch = greedyRegex.search('<To serve man> for dinner.>')
print('greedy match')
print(maxMatch.group())

# match newlines with dot character DOTALL to match all chars incl newlines
noNewlineRegex = re.compile('.*')
print('matches up to the first newline: ')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print('matches with all newlines: ')
print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \
\nUphold the law.').group())

# case insensitive matching with re.IGNORECASE or re.I argument
robocop = re.compile(r'robocop', re.I)
print('case insensitive matching: ')
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())

# substitute strings with sub method
namesRegex = re.compile(r'Agent \w+')
print('substitutions applied: ')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

# substitute but show first letter of matched
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print('substitute *** except 1st letter of matched string')
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.'))

# ignoring whitespace and comments in regex
phoneRegexComplex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}\
(\s*(ext|x|ext.)\s*\d{2,5})?)')
# spread regex over multiple lines
phoneRegexComplex2 = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)