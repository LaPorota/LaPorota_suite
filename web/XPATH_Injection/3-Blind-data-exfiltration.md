### INTRO

Funciona con el mismo criterio de las BLIND SQLI. Aunque, tristemente, no hay una funcion SLEEP.

### Funciones

| función | uso |
|---|---|
|Name() | Puede ser llamada en cualquier nodo y nos da el nombre del nodo    |
|Substring () | nos permite exfiltrar el nombre de un nodo un caracter a la vez  |
|string-length() | nos permite determinar el largo del nombre de un nodo |
|count() | Devuelve el número de hijos que tiene un nodo |

### Explotaciones

#### Extraer el length de un nodo

  invalid'+or+string-length(name/*[1]))=1+and+'1'='1
  
