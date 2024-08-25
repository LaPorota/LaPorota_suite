## Intro

Iam es el servicio/sistema que utiliza AWS para gestionar identidades. Se encarga de la autenticación y autorización de los usuarios, grupos e instancias dentro de AWS.

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
