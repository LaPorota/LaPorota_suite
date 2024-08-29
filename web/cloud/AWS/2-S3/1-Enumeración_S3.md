# Acciones

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

### Subir archivos

    aws cp .\archivo s3://nombre-del-bucket/

---

