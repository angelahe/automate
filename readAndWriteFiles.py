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
