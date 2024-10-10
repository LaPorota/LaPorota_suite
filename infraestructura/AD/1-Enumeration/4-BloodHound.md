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
