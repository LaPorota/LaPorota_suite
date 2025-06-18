## scan
    sudo nmap -sU --open -p 161 192.168.50.1-254 



### onesixtyone:

##### Install
    sudo apt install onesixtyone


##### Buscar etiquetas
    onesixtyone -c /opt/useful/SecLists/Discovery/SNMP/snmp.txt <ip>

nos va a devolver (si encuentra algo) información sobre el server. entre corchetes va a estar la etiqueta


## snmpwalk

    snmpwalk -v2c -c <etiqueta> <ip> -Oa 

La flag Oa traduce de hexa a ascii ;)

### Listar los usuarios

    snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25
### Listar procesos corriendo

    snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.4.2.1.2

### Listar software instalado

    snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.6.3.1.2

### Extended MIB
Podemos extender los MIB y de esta manera tener facultades extendidas como por ejemplo leer el contenido de archivos o scripts (lo realizará de manera automática)

    snmpwalk -c public -v1 192.168.50.151 NET-SNMP-EXTEND-MIB::nsExtendObjects

#### Si tenemos problemas porque no están los MIB:
    sudo apt install snmp snmp-mibs-downloader rlwrap -y
    git clone https://github.com/mxrch/snmp-shell
    cd snmp-shell
    sudo python3 -m pip install -r requirements.txt

### RCE

    https://hacktricks.boitatech.com.br/pentesting/pentesting-snmp/snmp-rce
