# Info

## Tipos de DACLS

| Tipo | desc |
|-----|-------|
| Generales |
| GenericAll |  Permite crear o eliminar child objects, eliminar un subtree, leer y escribir propiedades, examinar child objects, agregar o remover un objeto del directorio, o leer y escribir con extender rights. (todo el power sobre el objeto) |
| GenericExecute | Permite la lectura de permisos y listar un container object |
| Genericwrite |  permite escribir todas las propiedades de un objeto y realizar todas las validaciones de escritura de un objeto |
| GenericRead | Da permisos de lectura sobre un objeto, permite leer todas las propiedades del objeto |

 
Podemos listar de manera manual los ACL de un usuario usando el binario **dsacls**. El mismo es nativo.

### Listar ACLS que tienen las OU sobre un usuario

    dsacls.exe "cn=Yolanda,cn=users,dc=inlanefreight,dc=local"

### Listar ACLS que tiene un user en particular sobre el usuario

    dsacls.exe "cn=Yolanda,cn=users,dc=inlanefreight,dc=local" | Select-String "Pedro"

