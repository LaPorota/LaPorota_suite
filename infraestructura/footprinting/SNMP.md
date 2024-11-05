## scan
    sudo nmap -sU --open -p 161 192.168.50.1-254 



### onesixtyone:

##### Install
    sudo apt install onesixtyone


##### Buscar etiquetas
    onesixtyone -c /opt/useful/SecLists/Discovery/SNMP/snmp.txt <ip>

nos va a devolver (si encuentra algo) información sobre el server. entre corchetes va a estar la etiqueta


## sbnowalk

    snmpwalk -v2c -c <etiqueta> <ip>


### Listar los usuarios

    snmpwalk -c public -v1 192.168.50.151 1.3.6.1.4.1.77.1.2.25
### Listar procesos corriendo

    snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.4.2.1.2

### Listar software instalado

    snmpwalk -c public -v1 192.168.50.151 1.3.6.1.2.1.25.6.3.1.2
sudo apt install braa
