### INFO
TLSv1.3:
- Quitó soporte a parametros criptográficos inseguros.
- Redujo la complejidad
- Mejoraron el handshake para hacer más rápido el establecimiento de sesión
  

### Ejemplo de Cipher:

TLS_AES_128_GCM_SHA256

Solo especifica el algoritmo de encripción, el modo y la función hash usada para el algoritmo HMAC.

### Handshake

1) El cliente envía un mensaje "ClientHello"
   Este mensaje contiene el listado de ciphers soportados por el cliente a la vez que la clave del cliente.
2) El server responde con un  mensaje  "ServerHello" que confirma el  la clave que se va a usar y el cipher que se usará seleccionado dentro de la lista de ciphers enviado en el "ClientHello". Este mensaje también contiene la la clave del server.
3) El handshake concluye con los mensajes "ServerFinished" y "ClientFinished"
   
