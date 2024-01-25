### LSC / LXD

https://book.hacktricks.xyz/v/es/linux-hardening/privilege-escalation/interesting-groups-linux-pe/lxd-privilege-escalation

### DOCKER

Sumar un user al grupo de docker es sinónimo de darle permisos de root sin requerir passwd.
El usuario puede levantar un nuevo container con el /root en el nuevo volumen. De esta manera podemos recorrer el directorio dentro del docker (esto se puede usar con cualquier directorio)

    docker run -v /root:/mnt -it ubuntu

### Disk
Los usuarios participantes de este grupo pueden tener acceso a dispositivos dentro de /dev. Un atacante con estos privilegios puede usar debugfs para acceder al systema completo con permisos de root.

### ADM
Los miembros del grupo ADM pueden leer todos los logs dentro de /var/log. Esto no da permisos de root, pero sí permite leer logs que pueden contener información importante.
