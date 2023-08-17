import pymongo
import requests
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = myclient["Earthquack"]
mycolloction = mydatabase["distractions"]

api_endpoint = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'

try:
    response = requests.get(api_endpoint)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        #print(json.dumps(data,indent=4))  # Display the data
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")


mylist = json.dumps(data,indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(mylist)

insert_result = mycolloction.insert_many(mylist)

if insert_result.inserted_id:
    print(f"Data inserted with ID: {insert_result.inserted_id}")
else:
    print("Data insertion failed.")