# reading and writing to files

from pathlib import Path
import os

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
