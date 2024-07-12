### Cipher Suites

Definen el algoritmo criptográfico usado en la conexión. incluyendo la siguiente información:

- El algoritmo de intercambio de llaves
- El método utilizado para la autenticación
- El algoritmo de encriptación y el modo (da confidencialidad)
- El algoritmo de MAC (da integridad)

#### Ejemplo  de cipher:

    TLS_DH_RSA_WITH_AES_128_CBC_SHA256

Podemos desglozarlo en:
- El algoritmo de intercambio de llaves es Diffie-Hellman (DH)
- La autenticación del server es mediante RSA
- La encripción es en AES-128 enel modo CBC
- El algoritmo MAC es SHA256 HMAC

### Handshake

1) el  cliente envía un  mensaje "ClientHello":
   
   Este mensaje informa:
   - La última versión de TLS soportada por el cliente
   - Una lista de ciphers soportada por el cliente para realizar el intercambio
2) El server responde con un mensaje "ServerHello".
   El server elige  una versión igual o inferior a la versión de TLS dada por el cliente y elige uno de los ciphers dentro de la lista del "CLientHello".
3)El server brinda al cliente un certificado demostrando su identidad
4) Si se cnosensuó un cihper, el server  envía una nueva clave en el mensaje "ServerKeyExchange"
5) El server envía el mensaje "ServerHelloDone"
6) El cliente responde con el mensaje "clientKeyExchange" que contiene la clave compartida del cliente.
7) Las partes comparten un mensaje "ChangeCipherSpec" para indicar que de ahí en adelante todos los mensajes son encriptados usando la clave simétrica.
