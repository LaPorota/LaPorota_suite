## ENUMERATION

### Información de uid:
                id
Si el user se encuentra dentro de los grupos: LXD, DOCKER,DISK o ADM ir al módulo 3-GROUP ABUSING

### Info del kernel

    uname -a

siempre es bueno buscar exploits para el kernel antes de seguir con cualquier cosa. Es un easy win

### 1)Enumerar usuarios:
Las dos maneras de enumerar usuarios más certeras son:
##### Revisar los usuarios que tienen shells en el passwd:
        
        grep "*sh$" /etc/passwd

##### Revisar las carpetas dentro home

##### También lostar los usuarios logueados con el comando w(sí, w)

##### Listar los últimos logueos:
Esto nos sirve para saber si el servidor realmente se usa. Un server que se usa poco usualmente está mal configurado.

        lastlog

#### Enumerar las interfaces de red para determinar si hay otras subredes a las que podemos acceder

#### Buscar los grupos y sus miembros:

        cat /etc/group
##### podemos revisar un grupo en especial con getent:
        getent group <grupo>

##### Listar usuarios logeados

        who

#### Enumerar los archivos históricos:
Para el current user:
        history

Buscar archivos históricos:

        find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null



### 2)Enumerar servicios y apps:

##### Mostrar estado de las conexiones

        netstat

##### Paquetes instalados:

Podemos listar los paquetes instalados y guardarlos en un archivo para luego buscar vulnerabilidades:

         apt list --installed | tr "/" " " | cut -d" " -f1,3 | sed 's/[0-9]://g' | tee -a installed_pkgs.list

Buscar las vulnerabilidades en GTFObins:

        for i in $(curl -s https://gtfobins.github.io/ | html2text | cut -d" " -f1 | sed '/^[[:space:]]*$/d');do if grep -q "$i" installed_pkgs.list;then echo "Check GTFO for: $i";fi;done     

##### Version de Sudo:

        sudo -V

##### Binarios:

        ls -l /bin /usr/bin/ /usr/sbin/

### 3) Listar archivos de conf y carpetas/archivos ocultos.

#### Listar archivos de configuración

        find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null

#### Listar scripts

        find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"

#### Listar directorios con permisos para escribir:

    find / -path /proc -prune -o -type d -perm -o+w 2>/dev/null

#### Listar archivos con permisos de escritura:

    find / -path /proc -prune -o -type f -perm -o+w 2>/dev/null


#### Listar archivos temporales:

        ls -l /tmp /var/tmp /dev/shm

#### Listas discos no montados

         cat /etc/fstab | grep -v "#" | column -t

#### Enumerar procesos

        ps aux
#### Listar USBs conectados

        lsusb
#### Listar Archivos Abiertos

        lsof
#### Listar PCIs

        lspci

        
    
