# Info

Powerview tiene dos presentaciones: Su homonimo en script de powershell y SharpView. 

SharpView es una versiónm recreada en .Net de manera portable, tiene como beneficio una transacción de información menos transparente, lo cual la vuelve más útil al momento de atacar entornos reales sin que podamos ser agarrados infraganti por los pitufos.

Ambos usan los mismos argumentos y funciones. Puede variar la presentación del resultado.


Tabla de funciones para reconocimiento:

    https://powersploit.readthedocs.io/en/latest/Recon/

---

# Funciones básicas

## Referidas al dominio 

##### Obtener información de un dominio

    .\SharpView.exe Get-Domain
##### Enumerar las OUs del dominio

    .\SharpView.exe Get-DomainOU | findstr /b "name"

##### Enumerar usuarios que no necesiten kerberos preauth

    .\SharpView.exe Get-DomainUser -KerberosPreauthNotRequired

##### Enumerar computadoras dentro del dominio

    Get-DomainComputer | select dnshostname, useraccountcontrol  

##### Enumerar GPOs

    .\SharpView.exe Get-DomainGPO | findstr displayname

##### Enumerar relaciones de confianza

    Get-DomainTrust

---
## Referido a los usuarios

##### Convertir name a SID

    .\SharpView.exe ConvertTo-SID -Name sally.jones

##### Convertir Sid a Name

    .\SharpView.exe Convert-ADName -ObjectName S-1-5-21-2974783224-3764228556-2640795941-1724

##### Listar UACs de un user

    Get-DomainUser harry.jones  | ConvertFrom-UACValue -showall

##### Ver en qué computadoras los usuarios están logueados

    Find-DomainUserLocation

##### Listar ACLs de un user

    Get-DomainObjectACL -ResolveGUIDs -Identity * | ? {$_.SecurityIdentifier -eq $sid} 

---

## Referidas a las computadoras

##### Enumerar qué GPOs se linkean a una computadora

    Get-DomainGPO -ComputerIdentity WS01 | select displayname
##### Ver si nuestro user tiene permisos de administrador en otro host

    Test-AdminAccess -ComputerName SQL01
##### Ver si un host tiene SMB shares

    .\SharpView.exe Get-NetShare -ComputerName DC01

