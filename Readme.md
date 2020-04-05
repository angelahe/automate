# automate the boring stuff

to practice making and setting up python tools for automation
https://nostarch.com/automatestuffresources

current status: 
http://automatetheboringstuff.com/2e/chapter7/
file in progress: regex.py
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
errors in pip list install :
ERROR: pyobjc-framework-cocoa 6.1 has requirement pyobjc-core>=6.1, but you'll have pyobjc-core 5.2 which is incompatible.
ERROR: pyobjc 5.2 has requirement pyobjc-framework-Cocoa==5.2, but you'll have pyobjc-framework-cocoa 6.1 which is incompatible.

#advanced sys 
look for path
add to paths (need to find my bash profile file)

#vim 
#vim reminders
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
O - apprend above current line

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
