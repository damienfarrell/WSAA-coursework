# assignment01-currentweather.py
# A program which displays the specific weather data at certain coordinates.
# Author: Damien Farrell


import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 53.82,
    "longitude": -9.5,
    "current": "temperature_2m,wind_speed_10m,wind_direction_10m"
}

response = requests.get(url, params)
data = response.json()

temp = data["current"]["temperature_2m"]
temp_unit = data["current_units"]["temperature_2m"]

wind_direction = data["current"]["wind_direction_10m"]
wind_direction_unit = data["current_units"]["wind_direction_10m"]

print(f"The current temperature is {temp}{temp_unit}")
print(f"The current wind direction is {wind_direction}{wind_direction_unit}")