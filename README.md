# Project Biometrics 2020/2021:

group 5:
Carolien Braams,
Stijn Kramer,
Maartje Veraart,
Yannick Haveman


## How to run the code

We made Jupyter notebooks for our experiment. 
For this you need to install package manager pip:

``pip3 install jupyter``

if you want more information or use anaconda?
please check: https://jupyter.org/install

To install all the libraries and packages use command:
``pip3 install -r requirements.txt``

When everything is set up, use the command:
``jupyter notebook``
and jupyter will open up in your browser.


## How to use our git repository

Git uses branches, we use a branch to isolate development work without affecting other branches in the repository. You can use a GUI for git flows.
If you use the terminal this will help you:

Our default branch is **Master**. You switch between branches by:

``git checkout branchname``

To create a new branch:

``git checkout -b branchname``

use for your **branchname** your intials/feature you will work on eg. csb/siamesenetwork


To add your local files to git, in short:
```git
git add .
git commit -m "message"
git push
```

`git add .` for pushing everything or `git add specificfile.py` for a specific file only.

use `git status` to see all a overview of all you work

`git commit -m "message"` add in the message what changes you made eg. update gitignore 

``git push`` : For your first push to your own branch git will give another command with upstream in it. Use that one instead.

***
If your branch is behind the master branch because another teammate added new code to master, use:

``git merge master`` in your own branch to be up to date

!This would not have any merge conflicts since each branch should edit/make other features in other files.

If you have merge conflicts? one thing what you can do is:

``git stash`` this will stash your own edits, then do ``git pull`` and then do a ``git stash pop`` to pop your edits from the 
stash queue back to your branch. please google this if you are not confident what to do here. That is the best thing then to do
to dont loose code. Hopefully this will not happen often :)
