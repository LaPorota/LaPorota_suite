# Info

## Tipos de DACLS

| Tipo | desc |
|-----|-------|
| Generales |
| GenericAll |  Permite crear o eliminar child objects, eliminar un subtree, leer y escribir propiedades, examinar child objects, agregar o remover un objeto del directorio, o leer y escribir con extender rights. (todo el power sobre el objeto) |
| GenericExecute | Permite la lectura de permisos y listar un container object |
| Genericwrite |  permite escribir todas las propiedades de un objeto y realizar todas las validaciones de escritura de un objeto |
| GenericRead | Da permisos de lectura sobre un objeto, permite leer todas las propiedades del objeto |
| Standar |
| WriteDacl |  permite modificar el security descriptor de un objeto |
| WriteOwner | Permite modificar el owner de un objeto. El atacante puede tomar propiedad del objeto pero no puede traspasarlo a otros usuarios |
| ReadControl | Permite leer los datos del security descriptor de un objeto. |
| Delete | Permite eliminar el objeto |

| Extended access rights | 
| Display name | Common name | Desc |
|---------|---------|------|
| Reset Password | User-Force-Change-Password | Permite a un usuario cambiar el password de otro o su propio password sin conocer el anterior |
| Replicating Directory Changes | DS-Replication-Get-Changes | Requerido junto con DS-Replication-Get-Changes-All para hacer DCSync |
| Replicating Directory Changes All | DS-Replication-Get-Changes-All | Permite la replicación de los secrets del Domain |
| Add/Remove self as member | Self-Membership | Permite a un usuario agregarse o eliminarse a/de un grupo |
| Validated write to service principal name | Validated-SPN | permite editar el atributo SPN de un usuario |


# Enumerar ACLs desde windows

## DSACLS
Podemos listar de manera manual los ACL de un usuario usando el binario **dsacls**. El mismo es nativo.

#### Listar ACLS que tienen las OU sobre un usuario

    dsacls.exe "cn=Yolanda,cn=users,dc=inlanefreight,dc=local"

#### Listar ACLS que tiene un user en particular sobre el usuario

    dsacls.exe "cn=Yolanda,cn=users,dc=inlanefreight,dc=local" | Select-String "Pedro"

# Enumerar ACLS desde windows

### impacket-dacledit

#### Leer ACLS de un usuario

    impacket-dacledit -target {target} -dc-ip {DC_IP} {DOMAIN}/{USER}:'{PASS}'
