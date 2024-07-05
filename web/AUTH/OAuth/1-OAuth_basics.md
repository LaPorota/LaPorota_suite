### INFO

- Es un estandar que permite autorizaciones seguras entre servicios.
- Suele usarse en casos de SSO.
- No comparte las credenciales entre servicios

### Entidades

El protocolo OAuth está comprendido por las siguientes entidades:

| Entidad| Descripción |
|-----------|-----------|
|Resource owner  | La entidad dueña del recurso(usualmente el user     |
|Client     | El servicio que pide acceso al recurso     |
|Authorization service    | El servidor que autentica al rosource owner y da tokens de acceso al cliente     |
|Resource server    | El server que hostea los recursos a los que el cliente quiere acceder     |

### Flujo de comunicación del OAuth:

1. El client hace una petición de autorización al resource owner
2. El client recibe la autorización del resource owner
3. El client presenta la autorización al authorization server
4. El client recibe un access token del authorization server
5. el client presenta el access token al resource server
6. el cliente recibe el recurso pedido del resource server
