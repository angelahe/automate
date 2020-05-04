# strings
x = 'say hi to bob\'s mother'
# escape characters for '\n - new line \' - quote
# """ or ''' for multiline

x.islower()
x.isupper()
x.lower()
x.upper()
x.isalpha()
x.isalnum() #numbers and letters
x.isdecimal() #numbers only
x.isspace() #whitespace only
x.istitle() #strings are capitalized
x.startswith('Hello')
x.endswith('world')
','.join(['cats', 'rats', 'bats'])
'\n\n',join(['cats', 'rats', 'bats'])
'Hello'.rjust(10)
len('     Hello')
'Hello'.ljust(10)
'Hello'.ljust(20)
'Hello'.center(20, '=') #pad with spaces
'Hello      '.strip() #remove whitespace
'Hello      '.rstrip()
'      Hello   '.lstrip()
'SpamSpamBaconSpam'.strip('ampS')
spam.replace('e', 'XYZ')

import pyperclip

pyperclip.copy('Hello!!!!!!!!!!!')
pyperclip.paste()

#string formatting
#%s
name = 'Angela'
place = 'Bob\'s'
time = '6pm'
print('Hello %s, you are invited to a party at %s at %s' % (name, place, time))

string = "/foo13546897/bar/Atlantis-GPS-coordinates/bar457822368/foo/"
start = string.find('/bar/') + 5
end = string.find('/', start)
output = string[start:end]
