# Desde afuera

Podriamos enumerar un S3 mediante la herramienta cloud_enum

    cloud_enum -k <bucket_name> --quickscan --disable-azure --disable-gcp


Si encontramos un bucket que responde a nomenclaturas de ambientes:

    https://s3.amazonaws.com/LaPorota-public-asda/

podríamos probar cambiar el **public** por **private**.

Lo mismo en caso de ver **prod** por **dev** o **qa**

Podríamos automatizarlo utilizando clud_enum con una lista:

##### Creamos la lista

    for key in "public" "private" "dev" "prod" "development" "production"; do echo "LaPorota-$key-asda"; done | tee lista.txt

Luego:

    cloud_enum -kf lista.txt -qs --disable-azure --disable-gcp


## IMPORTANTE

Que un bucket no sea de acceso público, sus objetos dentro pueden llegar a ser públicos. **Hacer un FUZZ en los buckets privados buscando archivos**

# DEsde el CLI con credenciales

### Listar todos los buckets dentro de la cuenta actual

    AWS s3 ls
### Listar objetos dentro de un bucket

    aws s3 ls s3://Nombre-del-bucket/
    
##### Si queremos listar un bucket sin enviar credenciales

    aws s3 ls s3://nombre-del-bucket --no-sign-request

### Listar Objetos de un bucket de manera recursiva

    aws s3 ls s3://nombre-del-bucket/ --recursive

### Descarga de archivos

    aws s3 cp s3://nombre-del-bucket/archivo ./

##### hacerlo sin enviar credenciales

    aws s3 cp s3://nombre-del-bucket/archivo ./ --no-sign-request


### Subir archivos

    aws cp .\archivo s3://nombre-del-bucket/

---

