
Si es un circuito cerrado, agregamos la ip y el dns base al etc/hosts.


    dig ns <dns> @<dns>

agregamos los resultados como ns o ns1, ns2, etc al hosts


vamos a la carpeta de subbrute (git clone https://github.com/TheRook/subbrute.git >> /dev/null 2>&1)

agregamos el zonetransfer que queremos investigar:

    echo "ns.inlanefreight.htb" > ./resolvers.txt 

corremos subbrute

    ./subbrute.py <dns_base> -s ./names.txt -r ./resolvers.txt

agregamos lo encontrado al hosts.

    dig AXFR <subdominio_encontrado> @<dns_base>