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

### Insertar datos en una db:

        db.apples.insertOne({<field:<value>, <field>:<value>})

Podemos también insertar múltiples documentos agregando otro json separado por una coma:

        db.apples.insertOne({<field:<value>, <field>:<value>}, {<field:<value>, <field>:<value>})


### Listar todos los documentos en una colección:

        db.apples.find({})

### Seleccionar datos:

        db.apples.find({<field>:<value>})


