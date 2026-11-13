import json
import requests
api_url = "http://localhost:58000/api/v1/host"

# Ticket obtenido con 01_get-ticket.py, tomado de la variable de entorno NC_TICKET
headers={"X-Auth-Token": os.getenv("NC_TICKET", "NC-144-d131174a867340c3a5a8-nbi")}

resp = requests.get(api_url, headers=headers, verify=False)

print("Request status: ", resp.status_code)

response_json = resp.json()
print (response_json)
print()
print()
hosts = response_json["response"]

for host in hosts:
    print(host["hostName"], "\t", host["hostIp"], "\t", host["hostMac"], "\t", host["connectedInterfaceName"])