def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print('error found')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >=4:
        print('that is a lot of cats.')
    else:
        print('that is not that many cats')
except:
    print('you didn''t enter a number')