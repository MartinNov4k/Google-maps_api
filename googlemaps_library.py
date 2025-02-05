import googlemaps
API_KEY = "AIzaSyBHPg3UqPgyMP3yIFwgNuO9w7Q_BuvgZxA"



gmaps = googlemaps.Client(key=API_KEY)

directions = gmaps.directions("Praha", "Děčín", mode ="driving")

if directions:
    route = directions[0]["legs"][0]
    print(route["distance"]["text"])