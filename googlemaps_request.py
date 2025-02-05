import requests

API_KEY = "AIzaSyBHPg3UqPgyMP3yIFwgNuO9w7Q_BuvgZxA"

url = "https://maps.googleapis.com/maps/api/directions/json"

params = {
    "origin": "Děčín",
    "destination": "Praha",
    "mode": "driving",
    "key": API_KEY
}

response = requests.get(url,params=params)
print(response.status_code)
data = response.json()

if data["status"] == "OK":
        route = data["routes"][0]["legs"][0] 
        print(route["distance"]["text"])