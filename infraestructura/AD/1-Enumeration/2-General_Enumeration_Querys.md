# Enumeración de grupos:

### Obtener cantidad de grupos dentro de un dominio

     Get-ADGroup -Filter * | Measure-Object

### Obtener grupos de un dominio mediante LDAP

     Get-ADObject -LDAPFilter '(objectClass=group)' | select name
### Obtener grupos administrativos:

     Get-ADGroup -Filter "adminCount -eq 1" | select Name

### Obtener propiedades de un grupo

     Get-ADGroup -Identity "Help Desk" -Properties *


### Obtener miembros de un grupo

    net localgroup DNSAdmins /domain


---

# Enumeración de usuarios:

### Enumerar cantidad de usuarios de un dominio:

     Get-ADUser -Filter * | Measure-Object

### Enumerar cantidad de usuarios de un grupo:

     (Get-ADUser -SearchBase "OU=Employees,DC=INLANEFREIGHT,DC=LOCAL" -SearchScope Subtree -Filter *).count

### Enumerar usuarios con LDAP:

     Get-ADObject -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))' -Properties * | select samaccountname,useraccountcontrol

### Enumerar usuarios de confianza

     Get-ADUser -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' | select Name,memberof, servicePrincipalName,TrustedForDelegation | fl

### Enumerar un usuario por su nombre:

     Get-ADUser -Filter "name -eq 'sally jones'"

### Enumerar usuarios administrativos que no requeran preauth.

Estos usuarios pueden ser ASREPRoasted.

     Get-ADUser -Filter {adminCount -eq '1' -and DoesNotRequirePreAuth -eq 'True'}
### Enumerar usuarios administrativos con el ServicePrincipalName

Estos usuarios son potencialmente kerberosteables.

     Get-ADUser -Filter "adminCount -eq '1'" -Properties * | where servicePrincipalName -ne $null | select SamAccountName,MemberOf,ServicePrincipalName | fl

### Enumerar usuarios con el password en blanco

     Get-AdUser -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))(adminCount=1)' -Properties * | select name,memberof | fl

---

# Enumeración de computadoras:
     
### Enumerar cantidad de computadoras de un dominio

     Get-ADComputer -Filter * | Measure-Object

### Enumerar computadoras que tengan un nombre parcial:

     Get-ADComputer  -Filter "DNSHostName -like 'SQL*'"
### Enumerar computadoras de confianza

     Get-ADComputer -Properties * -LDAPFilter '(userAccountControl:1.2.840.113556.1.4.803:=524288)' | select DistinguishedName,servicePrincipalName,TrustedForDelegation | fl

