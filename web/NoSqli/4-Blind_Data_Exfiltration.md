## INFO

Al igual que las blind SQLI, debemos jugar con el guessing caracter por caracter.


## Manual:

Podemos hacer esto por medio de REGEX:

    "^valoraconsultar.\*"


#### ejemplo: 
supongamos que quisieramos saber el valor de un campo. Deberíamos consultar caracter por caracter hasta tener una respuestá distinta a las demas:

    user[$regex]=^char-a-probar.\*

Supongamos que el resultado de la primer prueba de caracteres fue "L". Lo dejamos fijo y empezamos a probar con el caracter siguiente

    user[$regex]=^Lchar-a-probar.\*
