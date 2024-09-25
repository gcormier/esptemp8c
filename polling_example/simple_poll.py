# make sure your esphome.yaml configuration file has web_server: section which will respond to REST API calls
import requests

url = "http://esptemp8c.local/sensor/0928"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    value = data.get("state")
    print("Value of sensor 0928:", value)
else:
    print("Error while retrieving data from the API")