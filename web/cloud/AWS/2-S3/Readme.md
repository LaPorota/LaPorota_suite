# Info

Los S3 son buckets. Son directorios de almacenamiento en la nube de AWS.

Cada objeto guardado en un bucket tiene dos componentes principales:

- Los datos del objeto (el objeto en sí)
- Un conjunto de metadatos (una serie de datos de clave-valor que describen los datos del objeto)

Los objetos de un S3 son inmutables. Pueden ser eliminados o reemplazados pero no modificados.

Cada objeto se identifica de manera única dentro de su bucket mediante una clave y, en algunos casos, su número de versión.

# Acceso a un objeto

Se accede a los objetos mediante una URL única compuesta por:

- Nombre del Bucket
- Región
- clave del objeto

    https://DOC-EXAMPLE-BUCKET.s3.us-west-2.amazonaws.com/photos/puppy.jpg

#Enumeración de buckets
Si encontramos un bucket que responde a nomenclaturas de ambientes:

    https://s3.amazonaws.com/LaPorota-public-asda/

podríamos probar cambiar el **public** por **private**.

Lo mismo en caso de ver **prod** por **dev** o **qa**


# Políticas de Bucket

- Solo el propietario tiene autoridad para asociar una política de bucket
- Los permisos definidos en una política de bucket afectan a todos los objetos dentro del bucket (en tanto estos sean propiedad del titular del bucket)
- Las políticas de bucket no pueden pesar mas de 20kb

#### Ejemplo de política 


    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PermitirSoloExtensionesDeImagen",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:PutObject",
                "Resource": "arn:aws:s3:::nombre-de-tu-bucket/*",
                "Condition": {
                    "StringLike": {
                        "s3:objectKey": [
                            "*.jpg",
                            "*.png",
                            "*.gif"
                        ]
                    }
                }
            }
        ]
    }

