### INFO

- El fin de este ataque es crear una discrepancia entre dos lógicas: "la lógica que verifica la firma" y "la lógica que extrae la información de autenticación".
- Se logra inyectando elementos XML en la SAML response que no invaliden la firma sino que confundan a la aplicación. Resultando esta última en el uso de la autenticación no firmada en vez de la correcta.
  

### Teoría

El idP puede firmar toda la SAML response o solamente la SAML Assertion. El elemento firmado por una "ds:Signature" es referenciado en la "ds:Reference". Ejemplo:

        <samlp:Response ID="_941d62a2c2213add334c8e31ea8c11e3d177eba142" [...] >
        	[...]
        	<saml:Assertion ID="_3227482244c22633671f7e3df3ee1a24a51a53c013" [...] >
        	    [...]
        	    <ds:Signature>
        	        <ds:SignedInfo>
        	            [...]
        	            <ds:Reference URI="#_3227482244c22633671f7e3df3ee1a24a51a53c013">
                        [...]
        	            </ds:Reference>
        	        </ds:SignedInfo>
        	    </ds:Signature>
        	    [...]
        	 </saml:Assertion>   
        </samlp:Response>

Como vemos en este caso, el nodo **ds:Reference** está firmando la SAML Assertion solamente y no toda la response debido a que en su URI la referencia.

### Locaciones de la firma

  | Lugar | Desc |
  |-------|------|
  |Enveloped | la firma es descendiente del recurso firmado |
  |Enveloping | La firma es predecesora del elemento firmado|
  |detached | la firma no es descendiente ni predecesora del recurso firmado (la firma no comparte nodo con el recurso firmado) |

El caso del ejemplo es, entonces, **enveloped**

### Iniciando el ataque:
Capturamos la SAML RESPONSE

##### dato:

Aunque es más engorroso para leer, hacer las siguientes modificaciones desde el inspector de burp, evita modificaciones no perceptibles que pueden llevarnos a fallar:

1) Copiamos la SAML Assertion y la pegamos antes de la Assertion original. De esta manera tendríamos 2 assertions.
2) Eliminamos la ds:Signature de la Assertion falsa.
3) modificamos el ID y los datos de autenticación.
4) Enviamos la request.

De esta manera, la lógica de la verificación de firmas encontrará la SAML assertion firmada y dará lugar a la lógica de autenticación que buscará la primer SAML assertion(la inyectada) presente en la response.

