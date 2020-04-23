# detect dates in DD/MM/YYYY format
# and then checks if they are valid dates

import re

# date regex

dateRegex = re.compile(r'''(
    (\d\d)/        # DD
    (\d\d)/        # MM
    (\d\d\d\d)     # YYYY
)''', re.VERBOSE)

tryagain = 'y'
maxThirtyMonths = {'04', '06', '09', '11'}

while tryagain == 'y':
    matches = []
    # get user input of dates
    print('enter some valid dates (DD/MM/YYYY): ')
    text = input()

    # check for if dates are valid, keep only the valid ones in the result list

    for groups in dateRegex.findall(text):
        # another way to do it if want different formatting
        # date = '-'.join([groups[0], groups[1], groups[2]])
        date = groups[0]
        validDate = True
        print('date found: ' + date)
        day = groups[1]
        month = groups[2]
        year = groups[3]
        # range is weird - stops at one less than the number specified
        if (int(month) in range(1, 13)) and (int(year) in range(1000, 3000)\
                and int(day) in range(1, 32)):
            if (month in maxThirtyMonths) and (int(day) not in range(1, 31)):
                validDate = False
            elif month == '02':
                print('year is '+ year)
                #find leap years
                if (int(year)%4 == 0) and \
                        ((int(year)%100 != 0) or \
                        (int(year)%400 == 0)):
                    print('is a leap year')
                    if int(day) not in range(1, 30):
                        validDate = False
                        print('day not in range : '+ day + ' for date ' + date)
                else:
                    if int(day) not in range(1, 29):
                        print('day not in range : '+ day + ' for date ' + date)
                        validDate = False
            else:
                if int(day) not in range(1, 32):
                    print('day not in range : '+ day + ' for date ' + date)
                    validDate = False
        else:
            print('date invalid for ' + date)
            validDate = False
        if validDate:
            matches.append(date)

    # print the valid dates
    if len(matches) > 0:
        print('valid dates found: ')
        print('\n'.join(matches))
    else:
        print('no valid dates found.')

    print('try again? (y/n) ')
    tryagain = input()




