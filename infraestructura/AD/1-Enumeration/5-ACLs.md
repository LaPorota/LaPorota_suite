# Info

Podemos listar de manera manual los ACL de un usuario usando el binario **dsacls**. El mismo es nativo.

### Listar ACLS que tienen las OU sobre un usuario

    dsacls.exe "cn=Yolanda,cn=users,dc=inlanefreight,dc=local"

### Listar ACLS que tiene un user en particular sobre el usuario

    dsacls.exe "cn=Yolanda,cn=users,dc=inlanefreight,dc=local" | Select-String "Pedro"

