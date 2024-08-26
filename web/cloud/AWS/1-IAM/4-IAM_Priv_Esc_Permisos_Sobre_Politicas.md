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

