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


