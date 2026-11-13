# Entorno de virtualización Python

# Pasos de instalación en Linux:

## 1. Clonación del proyecto

Desde la terminal ejecutar:

**git clone** <URL_del_repositorio> <nombre_de_la_carpeta_de_destino>

Luego ejecutar **cd** <nombre_de_la_carpeta_de_destino>. Esta carpeta será la raíz de nuestro proyecto en Python.

## 2. Creación del entorno virtual

Supongamos que el nombre que le damos al entorno virtual es **cisco**, entonces se creará una carpeta **cisco** con todas las librerías y dependencias necesarias paea nuestro proyecto. 

La manera de realizarlo es la siguiente:

# python3 -m venv <nombre_del_entorno>
Ejemplo: python3 -m venv cisco

Para activar el entorno escribimos **source cisco/bin/activate**, en la carpeta raíz del proyecto. El nombre del entorno virtual aparecerá entre paréntesis ().

## 3. Instalación de las dependencias, en este caso las librerías requests y tabulate

En la carpeta raíz de nuestro proyecto y dentro del entorno virtual escribimos: **pip install -r requirements.txt**

## 4. Selección del intérprete Python para nuestro entorno virtual

<img width="881" height="118" alt="image" src="https://github.com/user-attachments/assets/18c41d8e-d338-48b6-953c-b2499c57319f" />

<img width="736" height="412" alt="image" src="https://github.com/user-attachments/assets/2a795fcd-2cf8-47ef-a5a6-d21e09ce967f" />

Tal como se ve en la figura seleccionamos Python 3.10.12 (cisco) que se mostrará como entorno recomendado.

## 5. Desactivación del entorno virtual

Simplemente escribimos en la línea de comandos: **deactivate**



## Antes de ejecutar los scripts

- **Credenciales del controlador:** los scripts usan el usuario `cisco` y la clave `cisco123!`. Si en tu Network Controller creaste otro usuario, cambialos en `01_get-ticket.py` y en `04_tabulate.py`.
- **Ticket (X-Auth-Token):** `02_get-network-device.py` y `03_get-host.py` traen escrito un ticket de ejemplo que **no va a funcionar** en tu Packet Tracer, porque el controlador genera uno nuevo en cada sesión y vence. Ejecutá primero `01_get-ticket.py`, copiá el ticket que muestra y reemplazalo en el header `X-Auth-Token` de esos dos scripts. `04_tabulate.py` no necesita este paso: pide el ticket solo.


---

# TP N° 4 – Grupo 16 (Redes de Computadoras 3643)

Fork del repositorio de la cátedra con los scripts suministrados adaptados y el script propio del grupo.

## Cambios respecto de los scripts suministrados

Como el repositorio es público, **los usuarios y claves no quedan escritos en el código**. Los scripts los leen de variables de entorno:

| Variable | Uso | Ejemplo |
|---|---|---|
| `NC_USER` | Usuario del Network Controller (por defecto `admin`) | `admin` |
| `NC_PASS` | Clave del Network Controller | (la del grupo) |
| `NC_TICKET` | Ticket para `02` y `03`, obtenido con `01_get-ticket.py` | `NC-4-...-nbi` |

En Windows (PowerShell), antes de ejecutar:

```powershell
$env:NC_USER = "admin"
$env:NC_PASS = "<clave del controlador>"
python src/01_get-ticket.py
$env:NC_TICKET = "<ticket que mostró 01_get-ticket.py>"
```

## Qué hace cada script

| Script | Descripción |
|---|---|
| `src/01_get-ticket.py` | `POST /ticket`: obtiene el *service ticket* que se usa en el header `X-Auth-Token`. |
| `src/02_get-network-device.py` | `GET /network-device`: lista los dispositivos administrados (hostname, plataforma, IP de gestión). |
| `src/03_get-host.py` | `GET /host`: lista los hosts que ve el controlador (nombre, IP, MAC, interfaz a la que están conectados). |
| `src/04_tabulate.py` | Pide el ticket solo y muestra dispositivos y hosts en tablas con `tabulate`. |
| `src/05_inventario_csv.py` | **Script propio del grupo.** Obtiene el ticket, consulta `/network-device` y `/host` y exporta todo a `inventario.csv` (tipo, nombre, IP, MAC/plataforma, estado o equipo al que está conectado). También muestra un resumen por pantalla. Sirve para tener un inventario de la red que se abre con una planilla de cálculo y se puede comparar entre distintos momentos. |

## Requisitos

- Packet Tracer abierto con el `.pkt` del grupo y el acceso externo a la API habilitado (puerto 58000).
- `pip install -r requirements.txt` dentro del entorno virtual (en Windows: `python -m venv cisco` y `cisco\Scripts\activate`).
