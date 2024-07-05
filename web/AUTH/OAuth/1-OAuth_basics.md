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

##### el Auth server y el Resource server suelen ser el mismo host.

### Flujo de comunicación del OAuth:

1. El client hace una petición de autorización al resource owner
2. El client recibe la autorización del resource owner
3. El client presenta la autorización al authorization server
4. El client recibe un access token del authorization server
5. El client presenta el access token al resource server
6. El client recibe el recurso pedido del resource server

### Grants (concesiones) 

Las conceciones o "grants" más comunes de oauth son:
- Authorization code grant
- Implicit grant

#### Authorization code grant:

Es la más común y la más segura. El flujo es el mismo que el flujo de cominicación mencionado más arriba.

1. Authorization Request

   Usualmente se da por método GET y suele tener diferentes tipos de parámetros interesantes
   - Client_id: el ID único del cliente
   - Redirect_uri: La URL a la que el browser va a ser redirigido despues de una autorización exitosa
   - response_type: Para el authorization code grant suele ser seteada como "code"
   - scope: Indica los recursos a los que el cliente quiere acceder. (OPCIONAL)
   - state: Un random string similar a CSRF token para seguir el callback (OPCIONAL)
2. Resource owner Authentication
   El authorization server va a hacer una request de login al user y le va a pedir la autorización para brindar los recursos al client
3. Authorization code grant.
   El authorization server redirige al browser a la URL especificada en el redirect_uri de la authorization request.

   Esta request tiene dos parametros:
   - code: El codigo de autorización brindado por el authorization server
   - state: El token randomizado creado en la Authorization request para poder identificar y concatenar las requests
     
4. Access token request
   
