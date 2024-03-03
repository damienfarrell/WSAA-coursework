import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"

response = requests.get(url)
data = response.json()

file_path = "exchequer_account_(historical_series).json"
with open(file_path, 'w') as file:
    json.dump(data, file)