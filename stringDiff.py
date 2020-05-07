# find differences in strings

import difflib

cases=[('afrykanerskojęzyczny', 'afrykanerskojęzycznym'),
       ('afrykanerskojęzyczni', 'nieafrykanerskojęzyczni'),
       ('afrykanerskojęzycznym', 'afrykanerskojęzyczny'),
       ('nieafrykanerskojęzyczni', 'afrykanerskojęzyczni'),
       ('nieafrynerskojęzyczni', 'afrykanerskojzyczni'),
       ('abcdefg','xac')]

for a,b in cases:
    print('{} => {}'.format(a,b))
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))
    outputlist = [li for li in difflib.ndiff(a, b) if li[0] != ' ']
    print(f'outputlist {outputlist}')
    print()

# https://docs.python.org/2/library/difflib.html#difflib.ndiff
# can tokenize it use ndiff to compare list of strings (better than by single chars!)

diff = difflib.ndiff('one\ntwo\nthree\n'.splitlines(1), 'ore\ntree\nemu\n'.splitlines(1))
print (''.join(diff))