## Intro

Iam es el servicio/sistema que utiliza AWS para gestionar identidades. Se encarga de la autenticación y autorización de los usuarios, grupos e instancias dentro de AWS.

---

## Políticas

Una política de IAM es un documento que define los permisos sobre los recursos de AWS. Actúa como contrato entre AWS y una identidad(usuario, grupo o rol) o recurso.

### Estructura de una política

##### Ejemplo de política

    {
        "Version": "2012-10-17",
        "Statement": {
            "Effect": "Allow",
            "Action": [
                "iam:Get*",
                "iam:List*",
                "iam:Generate*"
            ],
            "Resource": "*"
        }
    }
#### Statement
- Cada política tiene uno o varios statement.
- Son bloques de construcción de las políticas.
- Incluye información sobre las acciones permitidas o denegadas, recursos a los que se aplican y bajo qué condiciones.

#### Effect
Se setea en Allow o Deny dependiendo de si las acciones consecuentes se encuentran permitidas o denegadas.

#### Action

Especifica la lista de acciones permitidas o denegadas. Son operaciones específicas de en los servicios de AWS.

#### Resourse

Define sobre qué recursos se aplican las acciones. Los recursos son especificados por un ARN(Amazon Resource Names)

#### Condition

Es opcional. Define las condiciones en las que se aplican las reglas del statement. Las condiciones pueden incluir: Fecha y dirección IP, entre otras cosas.


---


## Prefijo de ID de IAM

Las claves access_key_id de Iam tienen prefijos que distinguen su naturaleza:

|Prefijos	| Descripción |
|---|---|
|ABIA | AWS STS service bearer token|
|ACCA | Context-specific credential |
|AGPA | User group|
|AIDA | IAM user |
|AIPA | Amazon EC2 instance profile |
|AKIA | Access key ( son de larga duración. Están asociadas con usuarios de IAM, no caducan por defecto) |
|ANPA | Managed policy |
|ANVA | Version in a managed policy |
|APKA | Public key |
|AROA | Role |
|ASCA | Certificate |
|ASIA |Temporary (claves de acceso que se generan mediante el Securty Token Service (sts)) |
