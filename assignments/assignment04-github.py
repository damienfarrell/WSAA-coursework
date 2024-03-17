from github import Github
from config import apikey as cfg

old_name = "Andrew"
new_name = "Damien"
g = Github(cfg["apikey"])

repo = g.get_repo("damienfarrell/wsaa-coursework")
file_path = "assignments/name.txt"
contents = repo.get_contents(file_path)
file_content = contents.decoded_content.decode("utf-8")

def replace_name(file_content):
    updated_content = file_content.replace(old_name, new_name)
    return updated_content

updated_content = replace_name(file_content)

# Update the file in the repository
repo.update_file(file_path, f"Assignment 04: Updated name from {old_name} to {new_name}", updated_content, contents.sha)