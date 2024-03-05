import requests
from config import apikey as cfg


url = "https://github.com/damienfarrell/wsaa-coursework"

url_file_path = "https://github.com/damienfarrell/wsaa-coursework/blob/main/assignments/death_on_the_nile.txt"




apikey = cfg["apikey"]




with open(url_file_path, 'r') as file:
        file_data = file.read()



response = requests.get(url, auth=("token", apikey))

print(response.json)
print(file_data)