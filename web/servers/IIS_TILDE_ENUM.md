En algunas versiones de IIS se puede hacer una enumeración de directorios y archivos ocultos. Esto se debe a que el IIS server genera un "short file"

### Enumeration

##### Podemos usar IIS-shortname-scanner para realizar este proceso
https://github.com/irsdl/IIS-ShortName-Scanner

Necesita Oracle Java para correr: https://ubuntuhandbook.org/index.php/2022/03/install-jdk-18-ubuntu/

#### 1)Corremos el scanner contra el servidor:
    java -jar iis_shortname_scanner.jar 0 5 http://10.129.204.231/

#### 2)Fuerza bruta:
Con el shortname no podemos acceder al file, pero sí descubrir que se encuentra. Para esto deberemos crear una lista con el shortname para poder luego hacer fuerza bruta:

Supongamos que del scanner salió un file llamado: "TRANSF~1.ASP", deberíamos entonces agarrar el "transf"

    egrep -r ^transf /usr/share/wordlists/ | sed 's/^[^:]*://' > /tmp/list.txt

Luego hacemos fuerza bruta:

    gobuster dir -u http://10.129.204.231/ -w /tmp/list.txt -x .aspx,.asp
