#!/bin/bash

set -e

DIRNAME="./${1}"
# change mkrepo.py with your mkrepo.py path
python mkrepo.py $1
cd $DIRNAME
git init
#change username with your github username
git remote add origin git@github.com:username/$1.git
touch README.md
git add .
git commit -m "Initial commit"
git push -u origin master
