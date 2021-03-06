# reading and writing to files

from pathlib import Path
import os
import shelve
import pprint
from tests import myCats

#OS agnostic path - either WindowPath or PosixPath object
print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['abc.txt', 'def.csv', 'hij.docx']
for filename in myFiles:
    print(Path(r'/Users/me', filename))

# don't use this way
homeFolder = r'~/Users/AI'
subFolder = 'spam'
currentFolder = homeFolder+'\\'+subFolder
# alternate way
currentfolder2 = '\\'.join([homeFolder, subFolder])

# better so is os agnostic using / with Path
homeFolder2 = Path('/Users/AI')
subFolder2 = Path('spam')
currentfolder2_1 = homeFolder2 / subFolder2
print(str(currentfolder2_1))

# current working directory
Path.cwd()
print('working directory is ')
print(Path.cwd())
# change directory
os.chdir('/Users/angela/kata/2020code/automate/working')

print('working directory is now ')
print(Path.cwd())

# absolute and relative paths
# . this directory
# .. parent directory

# create new folder with os.makedirs() or several
#os.makedirs('/Users/angela/kata/2020code/automate/working/abc/def')

# create new folder with mkdir
#Path(r'/Users/angela/kata/2020code/automate/working/ghi').mkdir()

print('is current working directory absolute?')
print(Path.cwd().is_absolute())

print(Path('my/relative/path'))
print(Path.home())

# os.path.abspath(path) will return string of absolute path of the argument
#   to convert a relative path to absolute one

# os.path.isabs(path) returns true if it's an absolute path, false else

# os.path.relpath(path,m start) return string of relative path
#   from start path to path (use cwd if arg not provided)
print(os.path.abspath('.'))
print(os.path.relpath('/Users/angela/kata/2020code/automate', \
                      '/Users/angela/kata/2020code/jesttest'))

p = Path('/Users/angela/kata/2020code/automate/readAndWriteFiles.py')
print('path anchor')
print(p.anchor)
print('path parent')
print(p.parent)
print('path filename')
print(p.name)
print('path stem')
print(p.stem)
print('path suffix ' + str(p.suffix))
print('path drive ' + str(p.drive))

print('path parent 3 levels up: ' + str(p.parents[2]))

# can also use os.path - is an older library
print(str(os.path.basename(p)))
print(str(os.path.dirname(p)))

print('getting a paths dir name and base name together')
print(os.path.split(p))

# split file path on mac/linux 1st one will be ''
aFilePath = '/Users/angela/kata/2020code/automate/readAndWriteFiles.py'
print('all parts of the path as strings')
print(aFilePath.split(os.sep))
# or
listofparts = aFilePath.split(os.sep)
print(listofparts)
# find file sizes and folder contents
print('size in bytes of file')
print(os.path.getsize(aFilePath))

aDirectoryPath = '/Users/angela/kata/2020code/automate'
print('list all files in directory')
print(*os.listdir(aDirectoryPath), sep = '\n')

# find total size of all files in directory
totalSize = 0
for filename in os.listdir(aDirectoryPath):
    totalSize = totalSize + os.path.getsize(os.path.join(aDirectoryPath, filename))
print('total size of directory is ' +str(totalSize))

# mod a list of files using glob patterns (better than listdir)
# simplified form of regex
b_path = Path('/Users/angela/kata/2020code/automate')
print(b_path.glob('*'))
print("prints list of all files")
print(list(b_path.glob('*')))
print('prints list of txt files')
print(list(b_path.glob('*.txt')))
print('? can be for one character')
print(list(b_path.glob('*?s.txt')))

# iterate over generator that glob returns
for textFilePathObj in b_path.glob('*.py'):
    print(textFilePathObj) #print path as string
    #can di sinething with the text file...

# operation on every file in directory, either:
# os.listdir(p)
# or
# p.glob('*'

# check path validity
# p.exists() True if path exists or False if not
# p.is_file() True if path exists and is a file, False otherwise
# p.is_dir() True if path exists and is a directory, False otherwise
dirPath = Path('/Users/angela/kata/2020code/automate/tests')
thisFilePath = Path('/Users/angela/kata/2020code/automate/readAndWriteFiles.py')
notExistsDir = Path('/Users/folder/does/not/exist')
print('path exists')
print(dirPath.exists())
print('is a directory ')
print(dirPath.is_dir())
print('this directory does not exist')
print(notExistsDir.exists())
print('this is a file')
print(thisFilePath.is_file())
print('this is not a file')
print(dirPath.is_file())
print('this is not a directory')
print(thisFilePath.is_dir())
# and older library has os.path.isfile(path),
# os.path.isdir(path)

# file reading and writing
newFilePath = Path('/Users/angela/kata/2020code/automate/tests/spam.txt')
newFilePath.write_text('Hello my darling')
print('wrote Hello my darling to spam.txt')
print(p.read_text())

# more common way is to use open, read and write with file objects
helloFile = open(dirPath / 'hello.txt')
# or helloFile = open('/Users/angela/kata/2020code/automate/tests/hello.txt')
helloContent = helloFile.read()
print('hello content is :')
print(helloContent)

sonnetFile = open(dirPath / 'sonnet29.txt')
print('reading sonnet file into lines: ')
print(sonnetFile.readlines())

print('writing to bacon file')
baconFile = open(dirPath / 'bacon.txt', 'w')
baconFile.write('bacon is the best\n')
baconFile.close()
baconFile = open(dirPath / 'bacon.txt', 'a')
baconFile.write('bacon is most definitely not a vegetable.')
baconFile.close()
baconFile = open(dirPath / 'bacon.txt')
baconContent = baconFile.read()
baconFile.close()
print('content of baconfile')
print(baconContent)

# saving variables with shelve module
shelfFile = shelve.open('/Users/angela/kata/2020code/automate/tests/mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# can make changes to shelf value as if were a dictionary
shelfFile = shelve.open('/Users/angela/kata/2020code/automate/tests/mydata')
print('values in the shelf file cats dictionary')
print(shelfFile['cats'])
print('keys are:')
print(list(shelfFile.keys()))
print('values are:')
print(list(shelfFile.values()))
shelfFile.close()

# pretty print
# pprint.pprint() and pprint.pformat()

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
# should print: "[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
fileObj = open('/Users/angela/kata/2020code/automate/tests/myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

# importing the dictionary from myCats.py
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])
