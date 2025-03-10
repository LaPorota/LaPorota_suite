## Info

- Es una document-oriented DB.
- Guarda sus datos en colecciones de documentos compuestos por campo:valor.
- Los documentos de la misma son encodeados en BSON(un binario de Json).

### Ejemplo de un documento:

    {
      _id: ObjectId("63651456d18bf6c01b8eeae9"),
      type: 'Granny Smith',
      price: 0.65
    }
    
el campo _id se recerba como primary key del documento y debe ser único para toda una colección.

## Interactuar con una mongodb desde comandline:


        mongosh mongodb://<IP>:<PORT>

### Mostrar bases de datos:

        show databases

### Elegir una DB/Crear una DB

        use <db>

### Mostrar las colecciones dentro de una DB

        show collections

### Insertar datos en una db:

        db.<collection>.insertOne({<field:<value>, <field>:<value>})

Podemos también insertar múltiples documentos agregando otro json separado por una coma:

        db.<collection>.insertOne({<field:<value>, <field>:<value>}, {<field:<value>, <field>:<value>})


### Listar todos los documentos en una colección:

        db.<collection>.find({})


### Seleccionar datos:

        db.<collection>.find({<field>:<value>})


## Operadores de query:

### Comparativos:

| Operador | Descripción | Ejemplo |
|-----------|-----------|-----------|
| $eq   | Matchea los valores iguales a "x"|  type: {$eq: "Pink Lady"}    |
| $gt | Matchea los valores mayores a "X"     | price: {$gt: 0.30}     |
| $gte    | Matchea valores mayores o iguales a "x"     | price: {$gte: 0.50}    |
| $in    | Busca si un valor exite en un array específico     | type: {$in: ["Granny Smith", "Pink Lady"]}    |
| $lt    | Matchea valores menores a "x"    |   price: {$lt: 0.60}   |
| $lte    | Matchea valores menores o iguales a "x"     |   price: {$lte: 0.75}   |
| $nin    | Busca si un dato no se encuentra en un array específico     |  type: {$nin: ["Golden Delicious", "Granny Smith"]}    |

### Lógicos:

| Operador | Descripción | Ejemplo |
|-----------|-----------|-----------|
| $and    | Busca si dos condiciones se cumplen en una búsqueda     | $and: [{type: 'Granny Smith'}, {price: 0.65}]     |
| $not    | Busca documentos que no cumplan con las condiciones     | type: {$not: {$eq: "Granny Smith"}}    |
| $nor    | Busca documentos que no cumplan con alguna de las condiciones      | $nor: [{type: 'Granny Smith'}, {price: 0.79}]    |
| $or    | Busca documentos que cumplan alguna de las condiciones     |   $or: [{type: 'Granny Smith'}, {price: 0.79}]   |

### Evaluativos

| Operador | Descripción | Ejemplo |
|-----------|-----------|-----------|
| $mod    | Busca valores que divididos por un número específico dan como resultado un valor específico     | price: {$mod: [4, 0]}     |
| $regex    | Busca expresiones regulares     | type: {$regex: /^G.*/}     |
| $where    | Matchea documentos en base a expresiones javascript     | $where: `this.price < 0.70 && this.firstName.length === 6 and this.lastName.startsWith('R')`    |


### Ejemplo de búsqueda con operadores:
Buscamos en todos los documentos valores de la clave type" que empiecen con "G" y que sean de un "precio" menor a "0.70"

        db.<collection>.find({
            $and: [
                {
                    type: {
                        $regex: /^G/
                    }
                },
                {
                    price: {
                        $lt: 0.70
                    }
                }
            ]
        });


### Updatear documentos:

Las operaciones de actualización o update de documentos cuentan con dos operadores: uno de filtrado y uno de update. El filtro selecciona un documento mientras que el update indica el nuevo valor:

        db.<collection>.updateOne({type: "Granny Smith"}, {$set: {price: 1.99}})

        

### Remover documentos:

        db.<collection>.remove({price: {$lt: 0.8}})

