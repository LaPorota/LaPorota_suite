### INFO
- Son ataques criptográficos que resultan de mensajes de error referidos al padding cuando el modo de encripción CBC es usado. (ej: "Missing padding")
- Lo tienen todas las aplicaciones que no manejan la encriptación o desencriptación correctamente

 ### Block ciphers

 Algorítmo simétrico.

 Divide el input en bloques y los ecripta bloque a bloque. Para hacer esto es necesario que el tamaño del imput sea dibisible por el tamaño de los bloques. 

 Padding es la data agregada al imput para alcanzar el tamaño correcto para poder ser dividido por los bloques.
 ##### Ejemplo

 AES tiene un block size de 16 bits, si queremos encriptar un string de 30 bits, necesitamos agregar 2 bits de padding para poder dividirlo en los dos bloques necesarios.

 
 ### Idea del ataque

 El padding oracle attack aprovecha la información(mensaje  de error) dada por el servidor cuando este responde que un padding es usado de manera impropia. 

 Siendo esto, el atacante puede generar sus propios ciphertexts y hacer fuerza bruta buscando el bite de padding correcto que pueda dirigirnos a una fuga de información en texto plano.

 Esto permite al atacante desencriptar ciphertexts sin tener acceso a la clavce de desencriptación. En algunos casos, el atacante  puede encriptar sus propios datos sin necesidad de la llave.

#### Atacando

Para realizar este ataque podemos utilizar padbuster

    sudo apt install padbuster

Padbuster necesita:

- La URL a atacar
- Una muestra encriptada
- El block size (el block size lo vamos a tener que adivinar, los más comunes son 8 y 16)
- Si el cipher que queremos abusar está dentro de la cookie, tenemos que  indicárselo con la flag --cookies y la cookie
- Si es enviado mediante un POST debemos indicarlo con la flag -POST
- Si el datofinal está encodeado debemos indicarle el encoding con la flag -encoding y un value (en el caso de b64 es 0)

  padbuster http://127.0.0.1:1337/admin "AAAAAAAAAAAAAAAAAAAAAJQB/nhNEuPuNC8ox7cN1z0=" 16 -encoding 0 -cookies "user=AAAAAAAAAAAAAAAAAAAAAJQB/nhNEuPuNC8ox7cN1z0="


Padbuster va probar rellenar los bloques con el fin de adivinar cual es el bit que representa el padding y en base al mismo, desencriptar el mensaje.

Luego podemos generar nuestros propios cipertexts con el fin de obligar al sistema a realizar acciones indevidas:

Supongamos que el resultado de encriptación del ejemplo anterior fuera "user=user"; Podríamos generar nuestro propio ciphertext con la flag -plaintext indicando que "user=admin"

    padbuster http://127.0.0.1:1337/admin "AAAAAAAAAAAAAAAAAAAAAJQB/nhNEuPuNC8ox7cN1z0=" 16 -encoding 0 -cookies "user=AAAAAAAAAAAAAAAAAAAAAJQB/nhNEuPuNC8ox7cN1z0=" -plaintext "user=admin"

