import http.client
import json
import urllib.parse
from datetime import datetime, timedelta, timezone
import time



def make_request(origin,destination,API_KEY, departure_time):
    base_url = "/maps/api/directions/json"
    
    origin_encoded = urllib.parse.quote(origin)
    destination_encoded = urllib.parse.quote(destination)
    mode = "driving"

    params = (f"?origin={origin_encoded}"
            f"&destination={destination_encoded}"
            f"&mode={mode}"
            f"&departure_time={departure_time}"
            f"&traffic_model=best_guess"
            f"&key={API_KEY}")

    conn = http.client.HTTPSConnection("maps.googleapis.com")

    conn.request("GET", base_url + params)

    response = conn.getresponse()
    print(f"HTTP status code: {response.status}") 

    data = response.read().decode("utf-8")

    data_json = json.loads(data)

    conn.close()
    return data_json







def get_duration(origin, destination, interval, opakovani ):
    
    completed = 0
    API_KEY = "AIzaSyCdCLD3WGKfMoHqYnfb5gkUIry9MCh384g"
    
    
    
    
    tomorrow = datetime.now() + timedelta(days=1)
    departure_time_free_traffic = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 3, 0).timestamp()
    departure_time_free_traffic = str(int(departure_time_free_traffic))  
    
    
    
   
    data_json = make_request(origin, destination, API_KEY,departure_time_free_traffic)
    if data_json["status"] == "OK":
        route = data_json["routes"][0]["legs"][0]  
        duration_free = route["duration"]["value"]
        
            
    
    
    for i in range(opakovani):
        if i > 0:
            time.sleep(interval)
        
        now_utc = datetime.now(timezone.utc) 
        
        act_date_time = now_utc + timedelta(hours=1)
        
        act_date = act_date_time.strftime("%d.%m.%Y") 
        act_time = act_date_time.strftime("%H:%M")
        
        
        
      
        
        
        data_json = make_request(origin, destination, API_KEY,"now")
       

        if data_json["status"] == "OK":
            route = data_json["routes"][0]["legs"][0]  # První trasa, první úsek
            distance = route["distance"]["value"]
            duration_traffic = route["duration_in_traffic"]["value"]
            duration_traffic_text =route["duration_in_traffic"]["text"]
            delay = route["duration_in_traffic"]["value"] - duration_free
            
            print(f"Vzdálenost: {distance}")
            print(duration_traffic)
            
            print(delay)
            
        storage_file_name = origin + "-" + destination + ".csv"
        with open (storage_file_name,"a") as file:
            file.write(act_date)
            file.write(";")
            file.write(act_time)
            file.write(";")
            file.write(str(duration_traffic))
            file.write(";")
            file.write(duration_traffic_text)
            file.write(";")
            file.write(str(distance))
            file.write(";")
            file.write(str(delay))
            file.write("\n")
            
    completed+=1
    print(completed,"/", opakovani)
get_duration("Děčín", "Praha",10,1)