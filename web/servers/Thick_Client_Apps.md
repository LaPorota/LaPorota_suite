### INFO

- Están instaladas localmente en las computadoras.
- No necesitan de internet y son más performantes
- Las hay de 2 tipos:
  1) Two-tier:
     
     La app está instalada localmente y se conecta directamente a la base de datos
  2) three-tier:
     
     La aplicación está instalada localmente y se comunica con la DB mediante un server.


### EXPLOTACIÓN:
#### A) Comprender la arquitectura del mismo
##### 1) Debugueamos la app con x64dbg
###### Dejamos marcada solamente la casilla "Exit breakpoint"
##### 2) Vamos a file > open y seleccionamos la app que queremos debugear.
##### 3)Una vez está corriendo vamos a la pestaña "CPU" y con click derecho vamos a "follow in memory map"
##### 4)Buscamos Archivos tipo "MAP":
###### Los archivos MAP permiten a las aplicaciones acceder a archivos grandes sin tener que leerlos o escribirlos en memoria(son un lugar genial para buscar claves harcodeadas).
##### 5)Le damos doble click y podemos ver los magic bytes 
##### 6)Damos click derecho y la "address" y le damos a "dump memory file".
##### Lo corremos con strings y vemos qué info podemos obtener.

#### B explotar:

Una vez que ya sabemos la arquitectura del programa y en qué está escrito podemos buscar algun reverse de ejecutables propio del lenguaje en que está escrito, correrlo y buscar la información.

