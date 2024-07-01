### Pagina donde manipular JWTs

https://jwt.io

### Missing signature verification

En algunos casos las aplicaciones no validan la signature, con lo cual podremos modificar el token sin problema.


### None Algorithm Attack

Cuando usamos como algoritmo "none" la firma no es computada debido a la falta de algoritmo. Podríamos crear un nuevo token con CyberChef

##### 1) vamos a cyberchef

  https://gchq.github.io/CyberChef/
##### 2) Elegimos JWT sign y en signing algorithm elegimos none (borramos el secretkey)
##### 3) Copiamos el payload en texto plano en el input, manipulamos y en el output nos generará un token.


### BF the Signing Secret

Si el algoritmo del header fuera del tipo HS podríamos intentar adivinar el secret debido a que este es simétrico.

##### 1)guardamos el JWT en un .txt

    echo -n eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiaHRiLXN0ZG50IiwiaXNBZG1pbiI6ZmFsc2UsImV4cCI6MTcxMTIwNDYzN30.r_rYB0tvuiA2scNQrmzBaMAG2rkGdMu9cGMEEl3WTW0 > jwt.txt

##### 2) Intentamos romperlo con hashcat:

    hashcat -m 16500 jwt.txt /opt/SecLists/Passwords/Leaked-Databases/rockyou.txt

##### 3) crear un nuevo token:

Si logramos romper la secret key, podemos ir a jwt.io, manipular el token e ingresar la clave de seguridad para que nos genere un token válido nuevo.
