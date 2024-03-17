from github import Github
from config import apikey as cfg
import json

g = Github(cfg["apikey"])
repo = g.get_repo("damienfarrell/wsaa-coursework")

contents = repo.get_contents("assignments/")

file_info = []

with open("repo_contents.json", "w") as json_file:
    json.dump(file_info, json_file, indent=4)