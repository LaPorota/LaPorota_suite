# Enumeración de grupos:

### Obtener vantidad de grupos dentro de un dominio

     Get-ADGroup -Filter * | Measure-Object

### Obtener grupos de un dominio mediante LDAP

     Get-ADObject -LDAPFilter '(objectClass=group)' | select name

### Obtener propiedades de un grupo

     Get-ADGroup -Identity "Help Desk" -Properties *


### Obtener miembros de un grupo

    net localgroup DNSAdmins /domain

---
# Enumeración de usuarios:

### Enumerar cantidad de usuarios de un dominio:

     Get-ADUser -Filter * | Measure-Object

### Enumerar usuarios con LDAP:

     Get-ADObject -LDAPFilter '(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))' -Properties * | select samaccountname,useraccountcontrol

# Enumeración de computadoras:
     
### Enumerar cantidad de computadoras de un dominio

     Get-ADComputer -Filter * | Measure-Object
