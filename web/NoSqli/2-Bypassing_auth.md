## Caso de ejemplo:

Supongamos que tenemos un login que manda los datos por medio de un POST usando variables de "Username y password":

    username=mingo&password=mingita

Podríamos intentar injecciones que nos ayuden a bypassear el login mediante diferentes criterios:

### Autenticación negativa:

BUscamos un caso de resolución negativa. Luego agregamos a la variable del post la expresión [$ne]

    username[$ne]=mingo&password[$ne]=minga

De esta forma el loging buscara datos que no matcheen con los introducidos y nos dará el acceso como el primer dato de la lista(que usualmente es el admin :D ).

### Por expresiones regulares:

Podemos abusar de las expresiones regulares para poder traernos todos los registros y matcheará el primer registro como datos de login agregando la expresión [$regex]=.*

username[$regex]=.*&password[$regex]=.*

