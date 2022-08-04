#script
import requests
from pprint import pprint
from github import Github

class Invalid_input(Exception):
    def __init__(self):
      super().__init__()
    def __str__(self):
        return "Invalid input"


try:
    #signs the user in
    TOKEN : str = input("Github personal access token: ")
    g = Github(TOKEN)
    authed = g.get_user()

    #prompts for the repo name
    repo_name: str = input("repo name: ").replace(' ', '-')
    private_repo_question: chr = input ("private repo (Y/n): ")[0]
    if (private_repo_question.upper() == "Y"):
        private_repo: bool = True
    elif (private_repo_question.upper() == "N"):
        private_repo: bool = False
    else:
        raise Invalid_input()
except Invalid_input:
    print("\033[91m {}\033[00m" .format("Invalid Input"))
    exit()

try:
    #Create remote repo
    authed.create_repo(name=repo_name, private=private_repo)
    print("\033[92m {}\033[00m" .format(repo_name + " sucessfully created"))
except Exception as  e:
    #prints error message
    err: str = e.args[1]["message"]
    print("\033[91m {}\033[00m" .format(err))
