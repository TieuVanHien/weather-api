import requests

res = requests.get("https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&city=${location}&key=56ca9e58c28c4647bc4e4834f1fb6be6")

print(res.status_code)



