# SQLMAP

### Sobre db a atacar
SQLMAP suele confundirse al momento de atacar las bases de datos, devolviendo la db incorrecta. Asegurarse de, al momento de encontrar una inyección, correr el comando **--current-db** antes de intentar ir por las tablas. Nos evita grandes rabbit holes.

### Medir el risk

Nunca usar el risk cuando la petición es para un update, puede eliminar todo el contenido de la DB y estamos fritos.



