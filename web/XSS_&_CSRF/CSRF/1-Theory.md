### Intro

- CSRF (Cross-site request Forgery) es un ataque en el que el adversario hace realizar acciones inintencionales al browser de la víctima de manera forzada en un sitio donde está autenticado.
- Son realizados usualmente mediante un payload en un sitio controlado por el atacante. Esto requiere que la víctima visite el sitio del atacante.
- En los casos de exito, la request cross-origin es enviada con las cookies de sesión de la victima.

### Ejemplo:

- Un atacante tiene privilegios bajos en un sitio vulnerable a CSRF: **vulnerable.org**.
- El atacante crea un payload que corra en automático cuyo fin es, por medio de un formulario, envíe una request cross-site que actualice su usuario a administrador.
- Envía por diferentes medios (email, ingeniería social) el payload a un administrador de la página.
- El administrador lo ve y al instante se envía esta request con las cookies del administrador.
- La request es validada y el atacante se vuelve administrador en **vulnerable.org**

### Payload de ejemplo:

    <html>
      <body>
        <form method="GET" action="http://csrf.vulnerablesite.org/profile.php">
          <input type="hidden" name="promote" value="ATTACKER" />
          <input type="submit" value="Submit request" />
        </form>
        <script>
          document.forms[0].submit();
        </script>
      </body>
    </html>

### Métodos de defensa

#### CSRF tokens

- Son tokens únicos con valores random que deben ser incluidos en la request cuando se realizan cambios en una web.
- Deben ser impredecibles.
- Checkeado por el backend.
- No enviado en la cookie.
- De uso único.

En el ejemplo del payload anterior, el atacante debería introducir un parametro csrf_token con un valor random que (casi imposiblemente) fuera válido. De esta manera al enviar un token inválido, la página lo rejectaría.

#### HTTP headers

- Los browsers suelen agregar headers de **ORIGIN** o **REFERER** cuando se hace una request de cross-site. Un atacante no puede controlar esto.
- Los servidores pueden controlar estos headers para determinar si el sitio está dentro de una lista( blanca/negra)

#### SameSite Cookies

Es un atributo agregado a las cookies que determinan si la cookie puede ser enviada mediante cross-origin requests. 

##### Valores del atributo:

| valor | desc |
|---|---|
|none | la cookie es enviada mediante todas las cross-origin requests |
|lax | el browser solamente puede enviar la cookie en algunos casos. Solamente por métodos get y no puede ser enviada mediante JS |
|Strict | El browser no envía la cookie en ninguna request cross-origin. |


---
## Same Origin Policy

Es un mecanismo de seguridad implementado en los browsers para impedir las cross-origin. Especialmente que un JS corriendo en un origen pueda tener acceso a otro. 

### Origen

Se define mediantne el protocolo, el host(incluyendo dentro de él los subdominios) y el puerto de una URL. La Same Origin Policy aplica cuando dos URLs son distintas en alguna de estas tres propiedades.

### Excepciones

- img
- video
- scripts

---
---

## CORS

- Cross-Origin Resource Sharing
- Es un standard de W3C para definir excepciones en la Same-Origin policy.
- Establece los trusted origins y los verbos HTTP permitidos para el cross-origin.

### Tipos de request

#### Simple requests

- Pueden ser GET o HEAD sin custom headers
- Pueden ser POST sin custom headers, content-type, application/x-www-form-urlencoded, multipart/form-data o text/plain

#### Preflight requests
Son todas las que no son simple requests

# CONTINUARÁ...

### Headers de CORS:

| header | desc |
|----|---|
|Access-Control-Allow-Origin | Define las excepciones de la SOP para un origen específico |
|Access-Control-Expose-Headers | Define excepciones de la SOP para headers específicos |
|Access-Control-Allow-Methods | Define excepciones de la SOP para los verbos HTTP provenientes de una request preflight |
|Access-Control-Allow-Headers | Define excepciones de la SOP para los headers HTTP de una request preflight |
|Access-Control-Allow-Credentials | Si se setea en **true** define las excepciones de la SOP inclusive si la request cross-origin contiene credenciales (cookies o authorization headers) |
|Access-Control-Max-Age | Define cuanto tiempo va a ser capturada la información de los CORS-headers sin necesitar una nueva request preflight |





