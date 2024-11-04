# Intro
Si es un circuito cerrado, agregamos la ip y el dns base al etc/hosts.

### Buscar los nameserver records
    dig ns <dns> @<dns>

agregamos los resultados como ns o ns1, ns2, etc al hosts


### Buscar la ip de un host

    host url

### Buscar los MX (mail exchange/mail servers) de un host

    host -t mx url
### Buscar los TXT records de un host

    host -t txt url

### Bruteforcing de subdominios con bash

    for ip in $(cat list.txt); do host $ip.megacorpone.com; done

### Resolver de manera inversa hosts alojados en un rango de IPs

    for ip in $(seq <inicio> <fin>); do host 51.222.169.$ip; done | grep -v "not found"

# Herramientas
### DnsRecon

DnsRecon es una herramienta para automatizar la enumeración de DNS

#### Standar scan

    dnsrecon -d <url> -t std

#### Brute-force

    dnsrecon -d <url> -D ~/list.txt -t brt

### Dnsenum

Otra herramienta popular para enumerar DNS

### Enumeración básica

    dnsenum <url>

vamos a la carpeta de subbrute (git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1)

agregamos el zonetransfer que queremos investigar:

    echo "ns.inlanefreight.htb" > ./resolvers.txt 

corremos subbrute

    ./subbrute.py <dns_base> -s ./names.txt -r ./resolvers.txt

agregamos lo encontrado al hosts.

    dig AXFR <subdominio_encontrado> @<dns_base>
