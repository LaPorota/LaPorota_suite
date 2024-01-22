#### Buscar drupal en el código fuente:
     curl -s http://drupal.inlanefreight.local | grep Drupal

Otra manera de reconocerlo es por los "nodos", la forma de indexar contenido de drupal.

    http://drupal.inlanefreight.local/node/<id>


#### Cuentas:

Drupal reconoce 3 tipos de cuenta: Administrator, Authenticated user, anonymous.

#### Obtener versiones:
Si la versión de drupal es anterior a la 8 podemos conseguirla manualmente:

          curl -s http://drupal.inlanefreight.local/CHANGELOG.txt  | grep -m2 ""

Si la versión es >=8 el change log ya no está más disponible, tendremos que usar una app como droopescan:

          droopescan scan drupal -u http://drupal.inlanefreight.local


### Explotación 

#### Versión < 8
##### En versiones antiguas, debemos ir a módules y habilitar el "php filter".
##### Luego crear una Basic page con una shell desde el botón de "ADD content"

#### version > = 8
Desde la versión 8 en adelante, el "php filter" no viene instalado por defecto, tendremos que descargarlo

          wget https://ftp.drupal.org/files/projects/php-8.x-1.1.tar.gz

Luego vamos a el siguiente link, subimos el archivo y le damos a instalar, luego podemos continuar el ataque anterior:

          http://drupal.inlanefreight.local/admin/reports/updates/install


