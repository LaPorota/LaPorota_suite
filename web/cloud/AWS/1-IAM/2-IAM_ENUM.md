# Enumeración de usuarios

### Listar todos los usuarios
    aws iam list-users

### Enumeración de grupos a los que pertenece un usuario

    aws iam list-groups-for-user --user-name <user>

### Enumeración de Dispositivos de MFA

    aws iam list-virtual-mfa-devices

### Enumeración de políticas asociadas a un usuario

    aws iam list-attached-user-policies --user-name <user>

# Enumeración de grupos

### Listar todos los grupos del IAM

    aws iam list-groups

### Listar políticas adjuntas a un grupo

    aws iam list-attached-group-policies --group-name <group>

### Listar políticas que están incrustadas en un grupo

    aws iam list-group-policies --group-name <grupo>

# Enumeración de roles

### Listar todos los roles de IAM

    aws iam list-roles

### Listar políticas adjuntas a los roles

    aws iam list-attached-role-policies --role-name <rol>
### Listar políticas incrustadas en un rol

    aws iam list-role-policies --role-name <rol>

### Listar detalles específicos de un rol

    aws iam get-role --role-name <rol>

# Enumeración de políticas

### Listar todas las políticas de un IAM

    aws iam list-policies --profile <perfil>

### Obtener detalles de una política específica

    aws iam get-policy --policy-arn <arn> --profile <perfil>

### Enumerar versiones de una política

** Las políticas pueden ser actualizadas y se manejan por versiones. Enumerar versiones de políticas y sus detalles específicos nos permite acceder a versiones anteriores que incluyan problemas de configuración.**

    aws iam list-policy-versions --policy-arn <arn> --profile <perfil>

### Acceso a detalles de una versión en específico

    aws iam get-policy-version --policy-arn <arn> --version-id v<numero de versión> --profile <perfil>

    
