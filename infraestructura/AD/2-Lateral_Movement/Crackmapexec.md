# Info

Crackmapexec es una herramienta completa para enumerar AD.

Podemos ver los distintos protocolos que soporta con el help (-h) y tenemos un menú aparte de ayuda para cada protocolo si lo nombramos (**crackmapexec <prot> -h**)

# Enumeración

### Enumeración de usuarios:

    sudo crackmapexec smb <ip_DC> -u <user> -p <pass> --users

### Enumeración de grupos de dominio:
    sudo crackmapexec smb <ip_DC> -u <user> -p <pass> --groups

### Ver usuarios loggeados en otros hosts:

    sudo crackmapexec smb <ip_host> -u forend -p Klmcargo2 --loggedon-users

si el usuario con el que nos logueamos dice **(Pwn3d!)** quiere decir que es admin en ese host

### Enumerar shares en un host:
    sudo crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 --shares

podemos luego hacer un spidering a los shares que por lo menos tengan permiso de lectura


    sudo crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 -M spider_plus --share 'NOMBRE DEL SHARE'


Luego de hacer un spidering, se guardará un archivo con json de todo lo encontrado en:

    /tmp/cme_spider_plus/<ip of host>


Probar un rango de hosts buscando logins con users:
crackmapexec winrm 192.168.110.0/24 -u riley -p P@ssw0rd
