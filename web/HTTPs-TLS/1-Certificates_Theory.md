### INFO
- Los certificados permiten validar la idoneidad de un sitio
- Poseen información sobre el sitio
- Poseen la public key con la que se encriptará la información del sitio.

### Public key infraestructura

Cuando hablamos de encriptación asimétrica nos referimos a un método en el cual se utilizan dos llaves: **public key** y **secret/private  key**
| key | uso |
|------|------|
|Public | Se usa para encriptar los datos enviados|
|private | Se usa para desencriptar los datos |

La public key va a encontrarse en el cliente (front end) para que cualquiera que quiera comunicarse con el servidor pueda encriptar la información. La secret key va a estar resguardada dentro del servidor para poder desencriptar la información recibida.

### Certificate chain

Si bien,  los certificados pueden ser creados por cualquier persona, los que podríamos llamar "oficiales" son creados por **Certificate authorities** (CA) que son entes explicitamente habilitados para expenderlos.

La identidad de los certificados es provada por un CA certificate. Como todos los certificados son firmados por otro CA. Esta cadena se da hasta llegar a un  root CA.

Cuando entramos a un sitio, el browser valida toda la cadena de certificados.
