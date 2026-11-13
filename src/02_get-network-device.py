import json
import requests
api_url = "http://localhost:58000/api/v1/network-device"

# Ticket obtenido con 01_get-ticket.py, tomado de la variable de entorno NC_TICKET
headers={"X-Auth-Token": os.getenv("NC_TICKET", "NC-144-d131174a867340c3a5a8-nbi")}

resp = requests.get(api_url, headers=headers)

print("Request status: ", resp.status_code)

response_json = resp.json()
print()
print()
print (response_json)
print()
print()
networkDevices = response_json["response"]

for networkDevice in networkDevices:
    print(networkDevice["hostname"], "\t", networkDevice["platformId"], "\t", networkDevice["managementIpAddress"])
