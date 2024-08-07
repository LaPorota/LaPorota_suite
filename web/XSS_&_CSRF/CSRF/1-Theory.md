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

