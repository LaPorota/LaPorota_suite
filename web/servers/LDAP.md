### Info

- Suele correr en el puerto 389
- Se usa para gestionar directorios
- Usualmente se utiliza para gestionar autenticaciones en varios servicios a modo de "single sign on"

### Exploitation

Si vemos que en un servidor corre LDAP en el puerto 389 y a su vez un servicio web en el puerto 80, podríamos baypassear su login(el del servicio web) colocando un '*' en el user y el pass.
