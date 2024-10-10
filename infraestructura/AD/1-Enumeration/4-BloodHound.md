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

### Entornos monitorizados
En un escenario donde el entorno se encuentra monitorizado, deberíamos realizar dos recolecciones con SHarpHound.

Primero realizamos una de tipo DCOnly, luego analizamos los resultados buscando computadoras que sean interesantes, creamos una lista de las mismas y luego corremos una computerOnly agregando la flag --computerfile y el file creado de las computadoras

        .\SharpHound.exe -c ComputerOnly --computerfile <file>



