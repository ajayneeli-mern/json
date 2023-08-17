import requests
import json
from importlib.resources import path
import json
from unicodedata import name
import objectpath

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

querystring = {"nutrition-type":"cooking","category[0]":"generic-foods","health[0]":"alcohol-free"}

headers = {
	"X-RapidAPI-Key": "238b19a261msh6faff61eaf7274ap1c5b74jsn29182f756a83",
	"X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

try:
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        #data = json.dumps(response.json(),indent=4) # Parse JSON response  , never to reponse ,dumps for gettiing value from json
        data=response.json()['hints']
        
        
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

print(data)

json_file_path = 'hints.json'

# Write data to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)  # indent for pretty formatting

print(f"Data written to {json_file_path}")
