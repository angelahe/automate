# automate the boring stuff

to practice making and setting up python tools for automation
https://nostarch.com/automatestuffresources

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
