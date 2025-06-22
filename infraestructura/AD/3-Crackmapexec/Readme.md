# Modulos

Cada protocolo tiene una serie de módulos que se pueden desplegar con la flag -L

    crackmapexec smb -L

Para seleccionar un módulo utilizamos -M

    crackmapexec smb -M <modulo>

A cada uno de estos módulos podemos listarle las opciones con --options

    crackmapexec smb -M <modulo> --options

Luego elegimos la opción con -o

    crackmapexec smb -M <modulo> -o <opcion>

Las opciones se modifican de forma clave=valor

    crackmapexec ldap dc01.inlanefreight.htb -u grace -p Inlanefreight01! -M user-desc -o KEYWORDS=pwd,admin
    
# Status responses

CME nos va a dar respuestas en distintos casos de intentos de logueo:

#### Ej:
crackmapexec smb 10.129.203.121 -u julio peter -p Inlanefreight01!

SMB         10.129.203.121  445    DC01             [*] Windows 10.0 Build 17763 x64 (name:DC01) (domain:inlanefreight.htb) (signing:True) (SMBv1:False)
SMB         10.129.203.121  445    DC01             [-] inlanefreight.htb\julio:Inlanefreight01! **STATUS_LOGON_FAILURE** 
SMB         10.129.203.121  445    DC01             [-] inlanefreight.htb\peter:Inlanefreight01! **STATUS_PASSWORD_MUST_CHANGE**


| respuesta | definicion |
|----|----|
|STATUS_INVALID_LOGON_HOURS | Probar en otro horario |
|STATUS_INVALID_WORKSTATION  |  Probar en otra computadora |
|STATUS_PASSWORD_MUST_CHANGE |  El password es correcto pero "venció" y debemos cambiarlo|

### STATUS_PASSWORD_MUST_CHANGE

    smbpasswd -r 10.129.203.121 -U peter

