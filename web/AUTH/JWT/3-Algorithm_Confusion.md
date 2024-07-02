### Desc:

- Es un tipo de ataque que busca forzar a la app a usar un algoritmo diferente para verificar una nueva JWT's signature en vez de la usada para crearlo.
- Se usa en casos de algoritmos que usan claves asimétricas.

El sentido de este ataque es intentar "generar" o "impersonar" la clave publica con la que trabaja el token en el front.

### Herramientas

#### rsa_sign2n
##### Instalación

    git clone https://github.com/silentsignal/rsa_sign2n
    
    cd rsa_sign2n/standalone/
    
    docker build . -t sig2n

##### Correr la app

    docker run -it sig2n /bin/bash

##### Ataque

1. Dentro del contenedor encontraremos la herramienta jwt_forgery.py (corre con python3)
2. Deberemos pasarle dos tokens jwt para que la app pueda computarlos (para conseguirlos basta con loguearnos varias veces)

        python3 jwt_forgery.py token1 token2

3. El script creará varios tokens factibles de ser usados en el servicio web forzados al algoritmo HS256 y una RSA usada para crear la firma dentro de un archivo.pem. Habrá un .pem por cada token, podemos sacar el pem correspondiente en el orden que aparece su creción en el log coincidente con el orden de los tokens forjados por el script.
4. Probamos usar los tokens en la aplicación web y vemos si los acepta como válidos.
5. De ser aceptado algún token podremos ahora forjar uno nuevo manipulando el payload.
6. Vamos a cyberchef
   
    https://gchq.github.io/CyberChef/
   
7. Seleccionamos JWT sign.
8. En la sección de privatekey vamos a pegar el contenido de la RSA creada por el script agregando una línea al final de la public key (\n)
9. pegamos el payload en texto plano y lo editamos.
10. Usamos el token resultante para loguearnos en el servicio web y elevar nuestros privilegios

