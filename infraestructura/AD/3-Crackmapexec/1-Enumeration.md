# Info

Crackmapexec es una herramienta completa para enumerar AD.

Podemos ver los distintos protocolos que soporta con el help (-h) y tenemos un menú aparte de ayuda para cada protocolo si lo nombramos 

    crackmapexec <prot> -h

Para exportar podemos usar la función export pero está buggeada así que lo resolveríamos agregando el fullpath o

    --export $(pwd)/export.txt
---

# Enumeración

## Sin Credenciales

### Enumerar los HOST e información de los mismos dentro de una red

    crackmapexec smb 192.168.133.0/24

### Generar una lista con todos los HOST vulnerables a SMBRelay

    crackmapexec smb 192.168.1.0/24 --gen-relay-list relaylistOutputFilename.txt

### Abusando de los Null Session

##### Enumerar users del dominio
    crackmapexec smb 10.129.203.121 -u '' -p '' --users --export $(pwd)/users.txt

Luego transformamos lo extraido en una lista

    sed -i "s/'/\"/g" users.txt && jq -r '.[]' users.txt > userslist.txt
    
##### Enumerar grupos del dominio

    crackmapexec smb 10.129.203.121 -u '' -p '' --groups
##### Enumerar carpetas compartidas
    crackmapexec smb 10.129.203.121 -u '' -p '' --shares
##### Enumerar Password Policy
    crackmapexec smb 10.129.203.121 -u '' -p '' --pass-pol

--- 

## Con credenciales
### Enumeración de usuarios:

    sudo crackmapexec smb <ip_DC> -u <user> -p <pass> --users --export $(pwd)/users.txt

Luego transformamos lo extraido en una lista

    sed -i "s/'/\"/g" users.txt && jq -r '.[]' users.txt > userslist.txt

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
