### Ejemplo de query de autenticación web


    (&(uid=admin)(userPassword=minga))

### Wildcard Injection

Siendo que ldap usa el * como wildcard podemos utilizar este caracter en uno o ambos campos del login. (como siempre, de funcionar, nos validará como el primer user en la lista de users)

Tambien podemos utilizar el wildcard si tenemos un substring del nombre de un user:

Imaginemos que tenemos una empresa cuyos usuarios inicien con MSF y un número, al utilizar el wildcard al final de este,la app validará con el primer user que tenga esta nomenclatura.

    (&(uid=MSF*)(userPassword=*))

El * puede ir tanto delante, detrás o a ambos lados del substring.

### Universal true

Podemos inyectar un caso de universal true inyectando un or junto a un true(para esta búsqueda sí requerimos el nombre de un user válido) y agregamos un cierre de paréntesis al final de la contraseña:

    admin)(|(&

La query(del lado del server) quedaría:

    (&(uid=admin)(|(&)(userPassword=abc)))


