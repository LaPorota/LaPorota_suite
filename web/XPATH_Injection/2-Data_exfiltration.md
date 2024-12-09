### Intro

La data exfiltration funciona como las inyecciones SQL o el XSS en sus versiones avanzadas. Debemos intentar entender la query que se está haciendo al XML (en base al comportamiento) para inyectar código.

### Confirmando el Xpath injection

Podemos intentar una inyección booleana para determinar si la misma existe:

    SOMETHINGINVALID') or ('1'='1

### Exfiltrating data

Lo que necesitamos en primera instancia es conseguir todos los nodos del xml para poder determinar qué y como realizar consultas luego.

La forma más sencilla es agregar una nueva query que nos devuelva el contenido del XML en texto.

    <dato_x>+|+//text()

el pipe en XPATH es un similar al UNION en SQL.

Si tuvieramos varios parámetros pasándose al servidor, podríamos hacer inyecciones "compuestas"

    page.php?a=SOMETHINGINVALID')+or+('1'='1&b=../../..//text()


### Advanced Data exfiltration

No siempre es posible extraer el XML entero de una vez. En casos donde la aplicación se vea configurada para traer un número fijo de datos, la respuesta será en esa cantidad.

Debido a esto deberemos la profundidad del esquema del XML (los nodos y subnodos).

Para hacer esto debemos iterar recursivamente buscando exfiltrar datos recorriendo desde el root agregando /* y luego el index como si fuera un array [x].

/*= se mueve al root del documento y trae todo lo encontrado en el index pasado entre brackets

La inyección quedaría así:

    <dato_x>+|+/*[1]


Sin embargo usualmente los sitios están esperando un STRING y si de pronto esta indicación que le dimos referenciada a un subnodo que tiene dentro una profundidad, no habría un resultado puesto que desde el servidor nos traería un array.

Debemos entonces iterar hasta encontrar la profundidad del esquema completo del subnodo agregando nuevamente /*[1] hasta que traiga resultados. Funciona como una MATRIZ o ARRAY MULTINIVEL.

    <dato_x>+|+/*[1]/*[1]

Podremos entonces iterando una y otra vez llegar a la profundidad del esquema y exfiltrar todo cambiando los indexes para buscar datos concretos.

### Buscar etiquetas con la palabra password que tengan "a"

    %27)%5D/password%20%7C%20a%5Bcontains(a,%27
