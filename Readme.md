# automate the boring stuff

to practice making and setting up python tools for automation
https://nostarch.com/automatestuffresources

current status: 
http://automatetheboringstuff.com/2e/chapter8/
file in progress: validate.py

## set up git repo
inside new folder with code
```
git init
git add .
git commit -m 'initial commit'

```
go to github, click new repository, create
git remote add origin https://github.com/angelahe/automate.git
git push -u origin master

## setup

```bash
conda create -n auto_py python=3.7.4
conda activate auto_py
```

within the env, install the requirements:
```bash
pip install -Ur requirements.txt
```

did not work!  requirements file was missing from website and zip file, so try to set up
individually - maed my own requirements.txt file with install of these:

```bash
pip install --user send2trash==1.5.0
pip install --user requests==2.21.0
pip install --user beautifulsoup4==4.7.1
pip install --user selenium==3.141.0
pip install --user openpyxl==2.6.1
pip install --user PyPDF2==1.26.0
pip install --user python-docx==0.8.10 (install python-docx, not docx)
pip install --user imapclient==2.1.0
pip install --user pyzmail36==1.0.4
pip install --user twilio
pip install --user ezgmail
pip install --user ezsheets
pip install --user pillow==6.0.0
pip install --user pyobjc-framework-Quartz==5.2 (on macOS only)
pip install --user pyobjc-core==5.2 (on macOS only)
pip install --user pyobjc==5.2 (on macOS only)
pip install --user python3-xlib==0.15 (on Linux only)
pip install --user pyautogui
```
## other installs:
pip install --user pyperclip
pip install pyinputplus

## errors in pip list install :
ERROR: pyobjc-framework-cocoa 6.1 has requirement pyobjc-core>=6.1, but you'll have pyobjc-core 5.2 which is incompatible.
ERROR: pyobjc 5.2 has requirement pyobjc-framework-Cocoa==5.2, but you'll have pyobjc-framework-cocoa 6.1 which is incompatible.

## advanced sys 
look for path
add to paths (need to find my bash profile file)

#vim 
## vim reminders
https://vim.rtorr.com/
move: eg 4 j go down 4 lines
h j k l
H M L
w e b
W E B
0 - start of line
^ - 1st non blank char
gg - 1st line of doc
G - last line
5G - line 5
{ } - jump to next/prev paragraph
move screens: down 1, up 1, up 1 screen, down 1 screen, 1/2 screen
Ctrl+e y b f d u

insert:
r - replace character
i - before cursor
I - at beginning of line
a - after cursor
A - end of line
o - append new line below current
O - append above current line

cut/paste:
yy - copy line (2yy for 2 lines)
y$ - copy to end of line
p - paste
dd - delete 1 line, 2dd
dw - delete word
D - delete to end of line
d$ cut to end of line
x - delete
> shift text right
< shift text left

git
.gitignore
https://www.pluralsight.com/guides/how-to-use-gitignore-file

git rm --cached filename

useful links:
https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

## cool list printing
 print(*foundStrings, sep = ", ")
 or could print with newline:
 print(*foundStrings, sep = "\n")
 or can use map to convert item to string and then join them
 print(' '.join(map(str, foundStrings)))

## Regex summary:
\d - 0-9
\D - not 0-9
\w - a-z, 0-9, _
\W - not a-z, 0-9, _
\s - space, tab, newline
\S - not space, tab, newline
need to escape: \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)
[a-zA-Z0-9] - matches all lower/uppercase letters and numbers
\. match .
The | matches one of many expressions
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a non-greedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.
() in regex demarks the match groups for mo.group(), mo.group(0), mo.group(1)
re.VERBOSE - ignores whitespace and comments to spread regex over multi lines
regex.sub - substitute regex
re.IGNORECASE, re.I - case insensitive
re.DOTALL - matches even newlines
(r'.at') matches all but newline
(\btotal\b)(?!.*\1)  negative lookup of previous group ie last group not occur earlier
## pyinputplus library:
https://pyinputplus.readthedocs.io/.
help(pyip.inputChoice)

inputStr() Is like the built-in input() function but has the general PyInputPlus features. 
    You can also pass a custom validation function to it

inputNum() Ensures the user enters a number and returns an int or float, depending on if 
    the number has a decimal point in it

inputChoice() Ensures the user enters one of the provided choices

inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

inputDatetime() Ensures the user enters a date and time

inputYesNo() Ensures the user enters a “yes” or “no” response

inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and 
    returns a Boolean value

inputEmail() Ensures the user enters a valid email address

inputFilepath() Ensures the user enters a valid file path and filename, 
    and can optionally check that a file with that name exists

inputPassword() Is like the built-in input(), but displays * characters as the user types 
    so that passwords, or other sensitive information, aren’t displayed on the screen
    
args: min, max, lessThan, greaterThan, blank

inputCustom(customFunctionOfMine) - accepts string arg from user, raises exception if fails validation
    returns none if it should return it unchanged, non-None if returns different
    
## reading and writing files
 https://docs.python.org/3/library/os.path.html#os.path.join
 
 