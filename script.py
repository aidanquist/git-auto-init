#script
from email import message
import requests
from pprint import pprint
from github import Github



TOKEN : str = input("Github personal access token: ")

#signs the user in
g = Github(TOKEN)
authed = g.get_user()

#prompts for the repo name
repo_name: str = input("repo name: ")

try:
    #Create repo
    authed.create_repo(name=repo_name, private=True)
    print("\033[92m {}\033[00m" .format(repo_name + " sucessfully created"))
except Exception as  e:
    #prints error message
    err: str = e.args[1]["message"]
    print("\033[91m {}\033[00m" .format(err))
