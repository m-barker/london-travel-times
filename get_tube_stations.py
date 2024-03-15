import requests
import json

r = requests.get(
    "https://api.tfl.gov.uk/StopPoint/Mode/tube,dlr,overground,elizabeth-line"
)
full_data = r.json()
tube_stations = {}
for station in full_data["stopPoints"]:
    tube_stations[station["commonName"]] = {
        "lat": station["lat"],
        "lon": station["lon"],
    }

with open("data/tube_stations_lat_lon.json", "w") as f:
    json.dump(tube_stations, f)
