#script
import requests
import os
import sys
from sys import platform
from github import Github

#signs the user in
TOKEN : str = input("Github personal access token: ")
g = Github(TOKEN)
authed = g.get_user()

#prompts for the repo name
repo_name: str = str(sys.argv[0])
#prompt private or not
private_repo: bool = True if (sys.argv[0] == "private" or sys.argv[0] == "-p" ) else False

try:
    if (platform == "linux" or platform == "linux2" or platform == "darwin"):
        print()
    else:
        # Windows...
        print()

    #Create remote repo
    authed.create_repo(name=repo_name, private=private_repo)
    print("\033[92m {}\033[00m".format(repo_name + " sucessfully created"))
except Exception as  e:
    #prints error message
    err: str = e.args[1]["message"]
    print("\033[91m {}\033[00m".format(err))
