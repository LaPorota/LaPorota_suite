### Intro

El AWSCLI nos permite gestionar recursos de AWS desde la línea de comandos.

### Instalación

    sudo apt install awscli
### Estructura de los comandos

    aws <comando> <subcomando> [opciones y parámetros]

### Autenticación
Para autenticarnos en la nube de AWS necesitaremos crear un perfil.

    aws configure --profile <nombre del user/perfil>

Se iniciará el proceso para rellenar los datos correspondientes al perfil (acces key id, secret access key, zona y tipo de output)

Si queremos generar un usuario por defecto/maestro debemos hacer lo mismo pero sin agregar la flag --profile ni el user.

### Obtener información del usuario con el que estamos autenticados

    aws sts get-caller-identity --profile <user>

Usuario por defecto:

    aws sts get-caller-identity

---

### Interacción con EC2

#### Crear clave RSA para EC2

    aws ex2 creat-key-pair --key-name MyKeyPair --query 'key' --output text > MyKeyPair.pem

** importante ** Esta clave no se almacena en AWS

#### Crear instancia y correrla

    aws ec2 run-instances --image-id <imagen> --count 1 --instance-type <tipo_de_instancia> --key-name <key creada>

#### Listar instancias EC2

    aws ec2 describe-instances

#### Eliminar una instancia EC2

    aws ec2 terminate-instances --instance-ids <image_id_de_la_instancia>

#### Eliminar clave RSA

    aws ec2 delete-key-pair --key-name <nombre_de_la_key>

---

### Interacción con buckets S3

#### Creando un bucket

    aws s3 mb s3://<nombre_del_bucket>

#### Listar buckets

    aws s3 ls

#### Listar contenido de un bucket

    aws s3 ls s3://<nombre_del_bucket>

#### Cargar archivos en un bucket

    aws s3 cp <archivo> s3://<bucket>

#### Descargar un archivo de un bucket
    aws s3 cp s3://<bucket>/archivo ./

#### Borrar archivo de un bucket

    aws s3 rm s3://<bucket>/<archivo>
#### Borrar archivos de manera recursiva en un bucket

    aws s3 rm s3://<bucket> --recursive

#### Sincronizar contenido de un bucket en una carpeta local

    aws s3 sync s3://<bucket>/ <carpeta>/
#### Eliminar un bucket

    aws s3 rb s3://<bucket>

---

### Interacción con IAM

#### Crear grupo

    aws iam create-group --group-name <nombre>

#### Crear un usuario

    aws iam create-user --user-name <nombre>

#### Añadir un user a un grupo

    aws iam add-user-to-group --user-name <user> --group-name <grupo>

#### Obtener usuarios de un grupo

    aws iam get-group --group-name <nombre>

#### Asignar permisos a un usuario

    aws iam attach-user-policy --user-name <user> --policy-arn <arn>

La política con más privilegios en aws es

    arn:aws:iam::aws:policy/AdministratorAccess

#### Listar politicas de un usuario

    aws iam list-attached-user-policies --user-name <user>

#### Crear claves de acceso para un usuario

    aws iam create-access-key --user-name <user>

#### Listar usuarios diponibles

    aws iam list-users




