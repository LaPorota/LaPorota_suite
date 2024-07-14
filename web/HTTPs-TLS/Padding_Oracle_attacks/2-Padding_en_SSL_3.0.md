### esquema de padding  en SSL 3.0

- El último bite es el length del padding (exceptuandose a sí mismo— el bite— del length)
- Todos los bites de padding  pueden tener un valor arbitrario.

##### Ejemplo:

Asumiendo que usamos bloques de 8 bites y nuestro texto planotiene 4 bits: "DE AD BE EF". Requeriríamos 4 bits más de padding. Siendo que el  último bit del padding es el length del padding excluyendose a sí mismo, debería valer 03.

Nuestro valor final del stram debería ser: "DE AD BE EF 00 00 00 03"


### POODLE Attack

- El POODLE (Oracle On Downgraded Legacy Encryption) busca hacer un downgrade de el protocolo TLS usado a el SSL 3.0
- Puede ser ejecutado contra los tls v1.0 a v1.2
- Consta de dos partes: MIM y un Padding Oracle
#### MIM
- El atacante necesita interceptar el tráfico para forzar al cliente correr javascript malicioso y causar el downgrade de protocolos  al SSL 3.0 
#### PADDING Oracle

Envia requests al server variando el input para explotar la vulnerabilidad en el modo CBC de encryptación

### Realizando el ataque desde el étical Hacking

Si el server a atacar soporta SSL 3.0 Podemos  usar TLS-Breaker.

#### instalación

    sudo apt install maven
    git clone https://github.com/tls-attacker/TLS-Breaker
    cd TLS-Breaker/
    mvn clean install -DskipTests=true

#### Corriendo la tool de POODLE detection

    java -jar apps/poodle-1.0.1.jar -h


Podemos probar si el server es posiblemente vulnerable utilizando la flag -connect y especificando la ip y puerto(de ser necesario)

    java -jar apps/poodle-1.0.1.jar -connect 127.0.0.1:30001

Si el  server es vulnerable en el statuss nos dirá: "VULNERABILITY_POSSIBLE"

Aquí  la wiki para entender más de la tool: https://github.com/tls-attacker/TLS-Breaker/wiki/Poodle-Attack


### Prevensión

Se debe deshabilitar por completo el SSL 3.0 en  el server incluso para cuestiones Legacy.

Para desabilitarlo en apache2 usamos  la siuiente directiva:

    SSLProtocol all -SSlv3

