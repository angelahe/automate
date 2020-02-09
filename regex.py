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
print(mo.group()) #will find the phone number in the message

print(mo.findall)

# re.search
# re.group
# \d regex for numeric digit character

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #this groups the input
mo.group() #prints the phone number in the string
mo.group(1) #prints the first group in the string ie area code
mo.group(2) #prints the number

#add () to phone number like this
message2 = 'my number is (415) 555-2222'
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message2)
mo.group()

#use pipes to match one of several patterns as part of regex

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo.batRegex.search('Batmobile lost a wheel')
mo.group() #will print Batmobile
mo = batRegex.search('Batmotocycle lost a wheel')
mo.group() #will give nonetype obj has no attribute
mo.group(1) #to find which suffix was found
