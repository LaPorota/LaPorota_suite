1. Los JWT son tokens sesión
2. Constan de tres partes separadas por "." y encodeadas en base64:
    - Header
    - Payload
    - Signature
3. Suelen usarse para la autenticación y la autorización.

#### EJEMPLO DE JWT
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJIVEItQWNhZGVteSIsInVzZXIiOiJhZG1pbiIsImlzQWRtaW4iOnRydWV9.Chnhj-ATkcOfjtn8GCHYvpNE-9dmlhKTCUwl6pxTZEA


### Header:

Guarda información que permite interpretar el token. Usualmente tiene dos parametros con sus valores: "alg" y "typ".

typ= usualmente es JWT, indica el tipo de token que es.
alg= El algoritmo con que son encriptados los datos dentro del payload.

#### Usuales algorítmos con los alg:




| ALG |  ALGORITMO|
|-----------|-----------|
| HS256    | HMAC using SHA-256     |
| HS384    | HMAC using SHA-384     |
| HS512   | HMAC using SHA-512     |
| RS256    | RSASSA-PKCS1-v1_5 using SHA-256    |
| RS384   | RSASSA-PKCS1-v1_5 using SHA-384     |
| RS512    | RSASSA-PKCS1-v1_5 using SHA-512     |
| ES256    | ECDSA using P-256 and SHA-256     |
| ES384    | ECDSA using P-384 and SHA-384    |
| ES512    | ECDSA using P-512 and SHA-512     |
| PS256    | RSASSA-PSS using SHA-256 and MGF1 with SHA-256     |
| PS384    | RSASSA-PSS using SHA-384 and MGF1 with SHA-384     |
| PS512    | RSASSA-PSS using SHA-512 and MGF1 with SHA-512     |
