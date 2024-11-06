# Port scanning

## Netcat

### Recorrido básico de puertos TCP

    nc -nvv -w <tiempo de timeout> -z 192.168.50.152 <rango de puertos>
### Recorrido básico de puertos UDP

    nc -nv -u -z -w <tiempo de timeout> 192.168.50.149 <rango de puertos>

## Nmap

### Buscar hosts en una red

    nmap -sn 192.168.0.0/24

### Escaneo básico de los 1000 puertos más usados

    nmap <ip>

### Escanear servicios en puertos puntuales

    nmap -sV -p <1,2,3,4 o 1-4> <ip>

### Escanear servicios y buscar vulnerabilidades por default

    nmap -sV -p <1,2,3 o 1-4> -sC <ip>

### Realizar un SYN scan

Con esta técnica no terminará el handshacke. De esta manera **no se enviará la info a la capa de aplicación, con lo cual no hay logs ( en la aplicación) y será más rápido que el común**.

    sudo nmap -sS <ip>
### UDP scan

    sudo nmap -sU <ip>

##### Podemos combinar el UDP scan con el SYN scan

### Os guess

    sudo nmap -O 192.168.50.14 --osscan-guess
    
### Escaneo profundo

Podemos hacer un escaneo profundo agregando el OS detection, script scanning y traceroute con la opción -A


### Buscar NSE que sean exploits

    grep Exploits /usr/share/nmap/scripts/*.nse
