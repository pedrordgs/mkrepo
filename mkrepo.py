import sys
import os
from github import Github

dirName = "./" + str(sys.argv[1])
try:
    os.makedirs(dirName)
    print("Directory ", str(sys.argv[1]), " created")
except FileExistsError:
    print("Directory ", str(sys.argv[1]), " already exists")
    sys.exit()
#change username and password with your github username and password
g = Github("username","password")
g.get_user().create_repo(sys.argv[1])
