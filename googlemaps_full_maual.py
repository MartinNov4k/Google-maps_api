import http.client
import json
import urllib.parse


API_KEY = "AIzaSyBHPg3UqPgyMP3yIFwgNuO9w7Q_BuvgZxA"

origin = "Děčín"
destination = "Praha"


origin_encoded = urllib.parse.quote(origin)
destination_encoded = urllib.parse.quote(destination)
mode = "driving"

base_url = "/maps/api/directions/json"
params = f"?origin={origin_encoded}&destination={destination_encoded}&mode={mode}&key={API_KEY}"

conn = http.client.HTTPSConnection("maps.googleapis.com")

conn.request("GET", base_url + params)

response = conn.getresponse()
print(f"HTTP status code: {response.status}") 

data = response.read().decode("utf-8")

data_json = json.loads(data)

conn.close()

if data_json["status"] == "OK":
    route = data_json["routes"][0]["legs"][0]  # První trasa, první úsek
    print(f"Vzdálenost: {route['distance']['text']}")
