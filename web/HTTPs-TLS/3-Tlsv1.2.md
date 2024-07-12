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

