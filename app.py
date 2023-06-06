import requests
import json

def getData():
    # Make the API request
    url = "https://api.weatherbit.io/v2.0/current"
    params = {
        "lat": 35.7796,
        "lon": -78.6382,
        "city": "Calgary",
        "key": "56ca9e58c28c4647bc4e4834f1fb6be6"
    }
    res = requests.get(url, params=params)
    
    # Check if the request was successful
    if res.status_code == 200:
        data = res.json()
        with open("weather.json", "r+") as file:
            json.dump(data, file, indent=4)
        print("Data written to weather.json")
    else:
        print("Failed to retrieve data from the API")       

def printData():
    with open("weather.json", "r") as file:
        data = json.load(file)
        
        # Access the specific information from the JSON data
        city = data["data"][0]["city_name"]
        time = data["data"][0]["ob_time"]
        temperature = data["data"][0]["temp"]
        time_zone = data["data"][0]["timezone"]
        weather = data["data"][0]["weather"].get("description")
        country = data["data"][0]["country_code"]
        
        # Print the specific information
        print("City:", city)
        print("Time:", time)
        print("Country:", country)
        print("At Time Zone:", time_zone)
        print("Temperature:", temperature)
        print("Weather Status:", weather )

  
getData()
printData() 
