### Info

- OpenSSL es un  proyecto que implementa algoritmos criptográficos para comunicaciones seguras.
- Muchas distribuciones de linux  usan OpenSSL volviendolo esencial para las comunicaciones en internet.
- Al ser nativo de tantas distribuciones,  un bug o vulnerabilidad en este entorno se vuelve masiva y catastrófica.
- Podemos  usar OpenSSL para generar nuestras própias llaves, certificados convertirlos a diferentes formatos y realizar encriptación.


### Creando una RSA key de 2048 bits

    openssl genrsa -out key.pem 2048

### Descargar el certificado de cualquier web:

    openssl s_client -connect <site>:443 | openssl x509 > <file>.pem
    
### Convertir certificados de PEM a DER o PKCS#7

#### A DER
    openssl x509 -outform der -in <file.pem> -out <file>.der

#### A PKCS#7

    openssl crl2pkcs7 -nocrl -certfile <file.pem> -out <file>.p7

### Creando un  certificado

    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out selfsigned.pem -sha256 -days <días de duración del certificado>

### Desencriptar un archivo usando la private key

    openssl pkeyutl -decrypt -inkey <private_rsa> -in <File.enc> > decrypted.txt

    
