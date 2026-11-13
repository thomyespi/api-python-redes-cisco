"""inventario_csv.py - Script propio del Grupo 16 (TP N° 4, Redes 3643).

Obtiene un ticket de la API REST del Network Controller de Packet Tracer,
consulta los dispositivos (/network-device) y los hosts (/host) que ve el
controlador, y exporta todo a un archivo inventario.csv.

Uso:
    1. En Packet Tracer, habilitar el acceso externo a la API del controlador
       (puerto 58000) y dejar el .pkt abierto.
    2. Definir las credenciales del controlador como variables de entorno
       (o en el archivo .env, que NO se sube al repositorio):
           NC_USER=admin
           NC_PASS=<clave>
    3. python inventario_csv.py
"""
import csv
import os
from datetime import datetime

import requests

BASE = os.getenv("NC_URL", "http://localhost:58000/api/v1")
USER = os.getenv("NC_USER", "admin")
PASS = os.getenv("NC_PASS", "")

ARCHIVO = "inventario.csv"


def obtener_ticket():
    """POST /ticket -> devuelve el serviceTicket para el header X-Auth-Token."""
    r = requests.post(f"{BASE}/ticket", json={"username": USER, "password": PASS}, timeout=10)
    r.raise_for_status()
    return r.json()["response"]["serviceTicket"]


def consultar(recurso, token):
    """GET de un recurso de la API; devuelve la lista de la clave 'response'."""
    r = requests.get(f"{BASE}/{recurso}", headers={"X-Auth-Token": token}, timeout=10)
    r.raise_for_status()
    return r.json().get("response", [])


def main():
    token = obtener_ticket()
    dispositivos = consultar("network-device", token)
    hosts = consultar("host", token)

    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["tipo", "nombre", "ip", "mac / plataforma", "estado / conectado a"])
        for d in dispositivos:
            w.writerow([
                "dispositivo",
                d.get("hostname", ""),
                d.get("managementIpAddress", ""),
                d.get("platformId", ""),
                d.get("reachabilityStatus", d.get("collectionStatus", "")),
            ])
        for h in hosts:
            w.writerow([
                "host",
                h.get("hostName", ""),
                h.get("hostIp", ""),
                h.get("hostMac", ""),
                h.get("connectedNetworkDeviceIpAddress", ""),
            ])

    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] Inventario generado en {ARCHIVO}")
    print(f"  Dispositivos: {len(dispositivos)}")
    print(f"  Hosts:        {len(hosts)}")
    print()
    print(f"{'NOMBRE':<12} {'IP':<16} ESTADO")
    for d in dispositivos:
        print(f"{d.get('hostname', '-'):<12} {d.get('managementIpAddress', '-'):<16} "
              f"{d.get('reachabilityStatus', d.get('collectionStatus', '-'))}")


if __name__ == "__main__":
    main()
